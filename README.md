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
The scrapy scripts can be found in the directory `recipe_scraper/spiders`.

### 2. Datasets
The full datasets are too large to be stored online in this repository (up to 600 MB per file, 18 files). However, the data can be downloaded from my personal cloud storage using the provided script (`data/get_dataset.sh`). The data is provided as follows:

- chefkoch_XX.json
- kochbar_XX.json
- eatsmarter_XX.json

with XX denoting the month of its download date, ranging from 10 (=October 2017) to 03 (=March 2018). The datasets are largely redundant, because they are snapshots of the same websites taken over a period of six months.
This has been done in order to analyse changes on each website over that time frame.

#### Further Datasets
Similarly, download scripts for the trained word embeddings (`word_embeddings/get_embeddings.sh`) and the exported data subsets (`exports/get_exports.sh`) have been provided and can be executed in their respective folders.

### 3. Jupyter Notebook
Start Jupyter from console with `jupyter notebook` or through Anaconda Navigator. This will initiate a browser session, where you can browse and open the `.ipynb` files.

Coding with Jupyter goes step by step, which means that every line can be executed seperately for implementing changes and prototyping ideas.

#### Analysis Results
This repo contains the results of the data analysis (`Detailed_Analysis_*.ipynb`). They can be viewed for further insights, as they contain detailed analysis steps for each website, which are summarised in the thesis paper.

#### Generated Features and Word Embeddings
Some feature extractions are performed outside of the Analysis notebook, as they require more memory. The notebooks with he name `Trend_Dataset_*.ipynb` show how the datasets of each website need to be transformed to create a DataFrame that can be used to identify trending recipes.
The Notebook file `FastText_Model_Kochbar.ipynb` shows how text data can be extracted from the kochbar dataset to train word embeddings with the open source tool FastText. 

#### How to Read the Notebook Files
The notebook files can also be opened here on GitHub directly by just clicking on the respective file (read only).
If the notebook files (.ipynb) do not load, the .html files in the folder `html/` can be used for local read-only access.

### 4. Thesis Paper
This repo also contains the PDF file for the Master's thesis paper, which describes and summarises the complete project.
