# kochbar_spider.py
# run from project folder with console command:
# scrapy crawl kochbar -o kochbar.json
#
# author: Tolga Buz
# TU Berlin, 2017

import scrapy

class KochbarSpider(scrapy.Spider):
    name = "kochbar"
    start_urls = [
        'http://www.kochbar.de/rezepte/alle-rezepte.html?sort=userfav',
    ]

    def parse(self, response):
        '''
        This function opens the webpages that show all recipes page by page.
        For every recipe link on those pages, parse_recipe is being called,
        which extracts the detail information from each recipe page.
        The result will be stored into a .json file if the spider is run as described above.
        '''
        # For all 15 recipes per page: get link and start function parse_recipe
        for x in range(15):
            recipe = response.css("div.item-%d-content" % x)
            recipe_link = recipe.css('a::attr(href)').extract_first()
            yield response.follow(recipe_link, self.parse_recipe)
            		
        # Go to next page as long as there is one
        ## 1. get masked url
        next_p = response.css('span.masked-url::attr(data-url)')[-1].extract()
        print (next_p)
        ## 2. unmask url and append to full link
        next_p = next_p.replace('|', '/')
        next_p = next_p.replace('&amp;', '&')
        #next_page += next_p
        print (next_p)
        ## 3. if next_page exists, go there
        if next_p != []:
            yield response.follow(next_p, self.parse)

    def parse_recipe(self, response):
        '''
        This function opens a single recipe page and extracts its information.
        Some of the data is "hidden" in tables or similar structures, 
        which is why some of the structures need to be iterated.
        In particular, this affects infolist, preplist and inglist,
        which contain meta-information, preparation steps and ingredients.
        '''
        
        # info table consists of many empty text fields
        # first, we get all fields from that table and put them in a  list
        # then, we pick out difficulty, price and calories below
        infolist = max(response.xpath('//*[@id="kb-global-content"]/div[1]/div/div[6]/div/div[1]/div/table').xpath('.//td'),
                       response.xpath('//*[@id="kb-global-content"]/div[1]/div/div[5]/div/div[1]/div/table').xpath('.//td'),
                       response.xpath('//*[@id="kb-global-content"]/div[1]/div/div[4]/div/div[1]/div/table').xpath('.//td'),
                       response.xpath('//*[@id="kb-global-content"]/div[1]/div/div[3]/div/div[1]/div/table').xpath('.//td')).css('::text').extract()
        
        # clean infolist of empty entries
        info_filtered = []
        for x in range(len(infolist)):
            if ''.join(infolist[x]).startswith('\n'):
                pass
            else:
                info_filtered.append(infolist[x])      
        
        # the date can be either in /div[1]/div/div[5]/... or /div[1]/div/div[4]/...
        # thus, we need to check, which one is not empty
        # because only one of these options will contain a value per recipe page
        dateval = max(response.xpath('//*[@id="kb-global-content"]/div[1]/div/div[5]/div/div[1]/div/table').xpath('.//td/span/text()'),
                      response.xpath('//*[@id="kb-global-content"]/div[1]/div/div[4]/div/div[1]/div/table').xpath('.//td/span/text()'))[-1].extract()
       
        # We want to scrape the preparation steps as well
        preplist = max(response.xpath('//*[@id="kb-global-content"]/div[1]/div/div[5]/div/div[2]/div/div[3]').css('::text'),
                       response.xpath('//*[@id="kb-global-content"]/div[1]/div/div[4]/div/div[2]/div/div[3]').css('::text')).extract() 
        
        #this gives a list of Strings of which most are useless gaps
        # The line above returns us a list of strings that contains many useless strings that start with '\n'
        # We need to remove those elements
        preplist_filtered = ''
        for x in range(len(preplist)):
            preplist_filtered += ''.join(preplist[x])
        preplist_filtered = preplist_filtered.replace('\n','')
        preplist_filtered = preplist_filtered.replace('     ','')
        
        # It works the same way for the table of ingredients
        inglist = max(response.xpath('//*[@id="kb-global-content"]/div[1]/div/div[5]/div/div[1]/div/div[3]').css('::text'),
                      response.xpath('//*[@id="kb-global-content"]/div[1]/div/div[4]/div/div[1]/div/div[3]').css('::text')).extract()
        
        # Again, we need to filter the empty elements
        inglist_filtered = ''
        for x in range(len(inglist)):
            inglist_filtered += ''.join(inglist[x])
        inglist_filtered = inglist_filtered.replace('\n','')
        inglist_filtered = inglist_filtered.replace('     ','')
        
        minutes = max(response.xpath('//*[@id="kb-global-content"]/div[1]/div/div[4]/div/div[1]/div/table').xpath('//time').css('::text'),
                      response.xpath('//*[@id="kb-global-content"]/div[1]/div/div[5]/div/div[1]/div/table').xpath('//time').css('::text')).extract_first()
        
        # Some recipes do not shot the time needed for preparation, thus this response would the date of the first comment then.
        # This is why if the string minutes is too long (no recipe takes longer than 999 minutes), we set it to None
        if minutes is not None:
            if len(minutes) > 3:
                minutes = None
            
        # Some recipes have data about their rating, but not all of them
        rating = response.css('div.kb-recipe-image-gallery-rating-count::text').extract()
        if len(rating) == 2:
            number_votes = rating[1].replace('  ','').replace('\n','').split(' ')[0]
            avg_rating = rating[1].replace('  ','').replace('\n','').split(' ')[3]
        else:
            number_votes, avg_rating= 0,0            
        
        # The yield returns the following dictionary to the main parser function parse.
        yield {
                'name': response.css('div.kb-content-h1-wrapper').css('h1::text').extract_first().replace('\n','').replace('     ','').replace('    ',''),
                'subtitle': response.css('div.subheadline::text').extract_first(),
                'user': response.xpath('//*[@id="userinfo"]/span/a/text()').extract_first(),
                'date': dateval,
                'time_hrs': response.xpath('//*[@id="kb-global-content"]/div[1]/div/div[2]/div[1]/div/div[2]/div/div[2]/strong/text()').extract_first(),
                'time_mins': minutes,
                'comment_number': response.css('div.kb-recipe-performance-count::text').extract()[0],
                'clicks': response.css('div.kb-recipe-performance-count::text').extract()[1],
                'favorites': response.css('div.kb-recipe-performance-count::text').extract()[2],
                'difficulty': info_filtered[1],
                'price': info_filtered[5],
                'calories': info_filtered[11],
                'avg_rating': avg_rating,
                'number_votes': number_votes,
                'ingredients': inglist_filtered,
                'preparation': preplist_filtered
                }   
    