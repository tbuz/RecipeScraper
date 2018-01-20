# RecipeScraper
Example project for scraping German recipe websites

## Setup
For running this code, you need to install the following:

- Anaconda with Python 3 (includes Jupyter Notebook)
- `pip install scrapy pandas`

## Usage

### Scraper
Run the scraper for chefkoch and produce an output file called chefkoch.json:

`scrapy crawl chefkoch -o chefkoch.json`

Instead of chefkoch, you can crawl kochbar and eatsmarter with the same syntax.
Depending on your internet connection and the selected website, crawling can take 6-12 hours, because it extracts data from 200-450k different recipe pages.

### Jupyter Notebook
Start Jupyter from console with `jupyter notebook` or through Anaconda Navigator. This will initiate a browser session, where you can browse and open the `.ipynb` files.

Coding with Jupyter goes step by step, which means that every line can be executed seperately for implementing changes and prototyping ideas.

### Example Datasets
The full datasets are too large to be stored online in this repo (up to 600 MB per file). However, smaller subsets have been created to provide an understanding and sufficient overview of all three datasets.

### Analysis Results
This repo contains the visualised results of the data analysis as well. They can be viewed for further insights.
