# eatsmarter_spider.py
# run from project folder with console command:
# scrapy crawl eatsmarter -o eatsmarter.json
#
# author: Tolga Buz
# TU Berlin, 2017

import scrapy
import re

class EatsmarterSpider(scrapy.Spider):
    name = "eatsmarter"
    start_urls = [
        'http://eatsmarter.de/suche/rezepte?sort=voting&ft=',
    ]

    def parse(self, response):
        '''
        This function opens the webpages that show all recipes page by page.
        For every recipe link on those pages, parse_recipe is being called,
        which extracts the detail information from each recipe page.
        The result will be stored into a .json file if the spider is run as described above.
        '''
        # Get all links on the page (returns approx. 30 links)
        links = response.css('div.tile a::attr(href)').extract()
        # Iterate list of links and for each run parse_recipe
        for x in range(len(links)):
            yield response.follow(''.join(links[x]), self.parse_recipe)
            x += 1          
        
        # Go to next page as long as there is one
        ## 1. get url for the next page
        next_p = response.css('li.pager-next a::attr(href)').extract_first()
        ## 2. if next_page exists, go there
        if next_p != []:
            yield response.follow(next_p, self.parse)

    def parse_recipe(self, response):
        # Not all recipes have subtitles, which is why we need to consider those cases
        subtitle = ''
        if response.css('h2.subtitle::text').extract_first() is not None:
            subtitle = response.css('h2.subtitle::text').extract_first().replace('  ','').replace('\n','')
        
        statistics = response.css('a.recipe-tab::text').extract()
        number_comments = re.findall("\d+", statistics[2])[0]
        
        # Extract preparation steps 
        prep_list = response.css('div.field-name-field-preparation-steps div.field-name-field-text p::text').extract()
        
        # Some recipes have images and videos included in the preparation steps
        # Then, the structure is a bit different (if it is the case, set flag images to 1)
        images = 0
        if prep_list == []: 
            prep_list = response.css('div.field-name-field-preparation-steps div.field-name-field-text::text').extract()
            images = 1
            for x in range(len(prep_list)):
                prep_list[x] = prep_list[x].replace('  ','').replace('\n','')
            
        # Convert list to a single string by joining
        preparation = ''
        for x in range(len(prep_list)):
            preparation += ' '+(prep_list[x])
        
        yield {
                'name': response.css('h1.title::text').extract_first(),
                'subtitle': subtitle,
                'prep_time': response.css('div.field-preparation-time').css('div.traffic-light-value::text').extract_first(),
                'total_time': response.css('div.field-preparation-time-incl-wait').css('div.traffic-light-value::text').extract_first(),
                'comment_number': number_comments,
                'avg_rating': response.css('span.average-rating span::text').extract_first(),
                'total_votes': response.css('span.total-votes span::text').extract_first(),
                'difficulty': response.css('div.field-difficulty-level').css('div.traffic-light-value::text').extract_first(),
                'calories': response.css('div.traffic-lights-wrapper').css('div.traffic-light-calorie-value::text').extract_first(),
                'ingredients': response.css('div.ingredients span.ingredient a.name::text').extract(),
                'images': images,
                'preparation': preparation
                }
   
    