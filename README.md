# Python_Scrapy_basic
First_Web_Scraping_project


## Step 1:
```
+ Create virtual enviroment : python3 -m venv venv
+ Active virtual enviroment : source venv/bin/activate
+ Install scrapy inside venv : pip install scrapy
```

## step1 extend:
+ install scrapy proxy pool  (ver 0.1.7)
+ install scrapy random user agent
+ install scrapy fake user agent (not recommend)

## Step 2:
```
+ Scrapy will construct a web scaping project folder for you, with everything already setup. You just run a comman :

    - scrapy startproject amazon_scraper
```

## Step 3:
+ You just copy file setting.py and /spider/amazon.py 
+ scrapy crawl amazon -o test.csv
+ scrapy crawl amazon -o test.json (highly recommend using json)

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

-----
# Search in amazone
1.  Searching for a set product that has the same node id: https://www.amazon.com/b?node=10342349011
2.  Searching one product base on node id and product sku(Stock Keeping Unit): https://www.amazon.com/Speedball-Super-Value-Printing-Starter/dp/B000SKT0US
    + but in this situation, the product name in url is not the full name, so if you want to search by full name, you must encode the full name with function (urlencode): https://www.amazon.com/Speedball%20Super%20Value%20Block%20Printing%20Starter%20Kit%20%E2%80%93%20Includes%20Ink%2C%20Brayer%2C%20Lino%20Handle%20and%20Cutters%2C%20Speedy-Carve/dp/B000SKT0US


----
# user agent and proxy
1. Fake ip (using proxy) : https://github.com/rejoiceinhope/scrapy-proxy-pool
2. Fake user agent : https://github.com/alecxe/scrapy-fake-useragent
3. Pick random one user agent per request: https://pypi.org/project/scrapy-random-useragent/
4. link user agent for linux: https://developers.whatismybrowser.com/useragents/explore/operating_system_name/linux/
5. link rotate with list proxy: https://github.com/aivarsk/scrapy-proxies , https://github.com/TeamHG-Memex/scrapy-rotating-proxies
