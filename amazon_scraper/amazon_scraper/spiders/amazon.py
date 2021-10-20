import scrapy
import pandas as pd 
import os 
import urllib.parse

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
            self.product_name = urllib.parse.quote(li_product_name[i])
            self.product_sku = li_product_sku[i]
            self.node_id = li_node_id[i]

            url = "https://www.amazon.com/{}/dp/{}".format(self.product_name,self.product_sku)
            print(url)
            yield scrapy.Request(url=url, callback=self.parse_product_page)

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

        product_description = response.xpath('//div[@data-feature-name = "productDescription" and @data-template-name]//div[@id = "productDescription"]/p/text()').extract_first()
        try:
            product_description = product_description.replace("\n", "")
        except:
            product_description = product_description

        yield {
                 "product_name" : self.product_name,
                 "node_id" : self.node_id,
                 "product_sku" : self.product_sku,
                 "product_description" : product_description
             }