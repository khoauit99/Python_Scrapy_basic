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


-----
# Problem in amazon:
1. Page is lower level of bread_crum (child_hscode).

    ex : https://www.amazon.com/b?node=10342349011

2. Page of parent_hscode, it's root or just parent_hscode (have many child_hscode).

    ex : https://www.amazon.com/b?node=2258019011

    ex : https://www.amazon.com/b?node=706813011

3. Deliver to the nation which makes a decision numbers of sample will show in display.

4. Have a small number of category, so page will display relation but product in relation not belong to this node_id.

    ex : https://www.amazon.com/b?node=10342351011

5. First page show have n page , but can't push the button next.