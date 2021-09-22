# Python_Scrapy_basic
First_Web_Scraping_project


## Step 1:
```
+ Create virtual enviroment : python3 -m venv venv
+ Active virtual enviroment : source venv/bin/activate
+ Install scrapy inside venv : pip install scrapy
```

## Step 2:
```
+ Scrapy will construct a web scaping project folder for you, with everything already setup. You just run a comman :

    - scrapy startproject amazon_scraper
```

## Step 3:
+ You just copy file setting.py and /spider/amazon.py 
+ scrapy crawl amazon -o test.csv

----
# Task i will do in the future:
+ Crawl next page
+ multi process for scrapy
+ create file input_node_id, I just put node_id in amazon and crawl essential information which I need.
+ Fake ip through proxy, and increase concurrency_requeset.