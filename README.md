# RecipeScraper
Example project for scraping German recipe websites

## Setup
For running this code, you need to install the following:

- Anaconda with Python 3 (includes Jupyter Notebook)
- `pip install scrapy pandas numpy scipy fasttext matplotlib wordcloud`

## Usage

### 1. Scraper
Run the scraper for chefkoch and produce an output file called chefkoch.json:

`scrapy crawl chefkoch -o chefkoch.json`

Instead of chefkoch, you can crawl kochbar and eatsmarter with the same syntax.
Depending on your internet connection and the selected website, crawling can take 6-12 hours, because it extracts data from 200-450k different recipe pages.

### 2. Datasets
The full datasets are too large to be stored online in this repo (up to 600 MB per file, 18 files). However, the data can be downloaded from my personal cloud storage using the script provided in the folder `data/`. The data is provided as follows:

- chefkoch_XX.json
- kochbar_XX.json
- eatsmarter_XX.json

with XX denoting the month of its download date, ranging from 10 (=October 2017) to 03 (=March 2018).

### 3. Jupyter Notebook
Start Jupyter from console with `jupyter notebook` or through Anaconda Navigator. This will initiate a browser session, where you can browse and open the `.ipynb` files.

Coding with Jupyter goes step by step, which means that every line can be executed seperately for implementing changes and prototyping ideas.

#### Analysis Results
This repo contains the visualised results of the data analysis as well. They can be viewed for further insights, as they contain detailed analysis steps for each website, which are summarised in the thesis paper.

#### FastText Word Embeddings
The Notebook file `FastText Model Training.ipynb` shows how text data can be extracted from the kochbar dataset to train word embeddings. 

### 4. PDF file Master's Thesis
This repo also contains the PDF file for the Master's Thesis, which describes and summarises the complete project.


