import scrapy

queries = [10342348011,10342349011,10342351011]
#queries_1 = ['tshirt for men', 'tshirt for women']


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    start_urls = ['http://www.amazon.com']
    def start_requests(self):
        for query in queries:
            url = "https://www.amazon.com/b?node={}".format(query)
            print(url)
            yield scrapy.Request(url=url, callback=self.parse_product_page)



    def parse_product_page(self, response):

        node_id = response.xpath('//option[@selected= "selected" and @current]/@value').extract()
        node_id = node_id[0].replace("node=","")

        for products in response.xpath('//div[@data-asin and @data-uuid]'):
            product_sku = products.attrib['data-asin']
            xpath_of_product_name = '//div[@data-asin = "{}"]//span[@class = "a-size-base-plus a-color-base a-text-normal"]/text()'.format(product_sku)
            product_name = response.xpath(xpath_of_product_name).extract()
            
            yield {
                "product_name" : product_name,
                "node_id" : node_id,
                "product_sku" : product_sku,
            }

        next_page = response.xpath('//li[@class = "a-last"]/a/@href').extract_first()
        next_page = "https://www.amazon.com{}".format(next_page)
        if next_page is not None:
            yield response.follow(next_page,callback = self.parse_product_page)