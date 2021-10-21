import scrapy
import pandas as pd 
import os 
import urllib.parse
import random

# queries = [10342348011,10342349011,10342351011]
# check_queries = [13764241, 13299331]
#queries_1 = ['tshirt for men', 'tshirt for women']


file_data_name = input("Name of file data: ")
start_line = int(input("Enter number line start: "))
end_line = int(input("Enter number line end: "))

data_path = os.getcwd()+"/amazon_scraper/data/{}".format(file_data_name)
full_data = pd.read_csv(data_path)
full_data = full_data[start_line:end_line]

li_product_name = full_data["product_name"].tolist()
li_product_sku = full_data["product_sku"].tolist()
li_node_id = full_data["node_id"].tolist()
proxies_list = ["128.199.109.241:8080","113.53.230.195:3128","125.141.200.53:80","125.141.200.14:80","128.199.200.112:138","149.56.123.99:3128","128.199.200.112:80","125.141.200.39:80","134.213.29.202:4444"]

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    start_urls = ['http://www.amazon.com']

    def start_requests(self):
        # for query in queries:
        #     url = "https://www.amazon.com/b?node={}".format(query)
        #     print(url)
        #     yield scrapy.Request(url=url, callback=self.parse_product_page)

        for i in range(len(li_product_name)):
            proxies = 'http://{}'.format(random.choice(proxies_list))
            self.product_name = li_product_name[i]
            #url_encode_product_name = urllib.parse.quote(self.product_name)
            self.product_sku = li_product_sku[i]
            self.node_id = li_node_id[i]


            url = "https://www.amazon.com/{}/dp/{}".format(self.product_name,self.product_sku)
            print(url)
            yield scrapy.Request(url=url, callback=self.parse_product_page)
            #request.meta["proxy"] = "http://165.227.186.129:80"    

    def parse_product_page(self, response):

        # node_id = response.xpath('//option[@selected= "selected" and @current]/@value').extract_first()
        # #node_id = node_id[0].replace("node=","")

        # for products in response.xpath('//div[@data-asin and @data-uuid]'):
        #     product_sku = products.attrib['data-asin']
        #     xpath_of_product_name = '//div[@data-asin = "{}"]//span[contains(@class , "a-color-base a-text-normal")]/text()'.format(product_sku)
        #     #xpath_of_product_name = '//div[@data-asin = "{}"]//span[@class = "a-size-base-plus a-color-base a-text-normal"]/text()'.format(product_sku)
        #     product_name = response.xpath(xpath_of_product_name).extract_first()
            
        #     yield {
        #         "product_name" : product_name,
        #         "node_id" : node_id,
        #         "product_sku" : product_sku,
        #     }

        # next_page = response.xpath('//li[@class = "a-last"]/a/@href').extract_first()
        # next_page = "https://www.amazon.com{}".format(next_page)
        # if next_page is not None:
        #     yield response.follow(next_page,callback = self.parse_product_page)

        # print(response.status)

        # tmp_product_name = self.product_name
        # tmp_product_sku = self.product_sku
        # tmp_node_id = self.node_id

        if response.status == 200:
            print("Trang thai la: {}".format(response.status))

            product_description = response.xpath('//div[@data-feature-name = "productDescription" and @data-template-name]//div[@id = "productDescription"]/p/text()').extract()
            product_name = response.xpath('//span[@id = "productTitle"]/text()').extract_first()
            link_product = response.xpath('//link[@rel = "canonical"]/@href').extract_first()
            try:
                product_name = product_name.replace("\n","")
                if product_description[0] == "\n":
                    product_description = response.xpath('//div[@data-feature-name = "productDescription" and @data-template-name]//div[@id = "productDescription"]/p/span/text()').extract()
            except:
                product_description = product_description
            
            try:
                stt = link_product.find("/dp/")+4
                product_sku = link_product[stt:]

            except:
                product_sku = None
                print("ERROR FIND: {}".format(product_name))
                print(link_product)

        else:
            product_description = "404"
            product_name = "404"
            product_sku = "404"

        yield {
                "product_name" : product_name,
                #  "node_id" : tmp_product_sku,
                "product_sku" : product_sku,
                "product_description" : product_description
             }