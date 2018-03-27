# RecipeScraper
Data Science Project for Scraping German Recipe Websites

This repo contains the source code, scripts and pdf file for the Master's thesis:  

**Creating Business Value with Multi-Domain Data Analysis on Web-Scraped Data**  
**(from the Largest German Recipe Platforms)**

Author: Tolga Buz  
Programme: M.Sc. Industrial Engineering  
Supervision:  
Chair of Information and Communication Management  
Institute of Technology and Management  
Technical University of Berlin

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

#### Generated Features and Word Embeddings
Some feature extractions are performed outside of the Analysis notebook, as they require more memory. The notebooks with he name `Trend_Dataset_*` show how the datasets of each website need to be transformed to create a DataFrame that can be used to identify trending recipes.
The Notebook file `FastText Model Training.ipynb` shows how text data can be extracted from the kochbar dataset to train word embeddings with the open source tool FastText. 


### 4. PDF file Master's Thesis
This repo also contains the PDF file for the Master's Thesis, which describes and summarises the complete project.
