import scrapy

queries = [10342349011]
queries_1 = ['tshirt for men', 'tshirt for women']


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    start_urls = ['http://www.amazon.com']
    def start_requests(self):
        for query in queries:
            url = "https://www.amazon.com/b?node=1069738"
            print(url)
            yield scrapy.Request(url=url, callback=self.parse_keyword_response)


    def parse_keyword_response(self, response):
        products = response.xpath('//*[@data-asin]')

        for product in products:
            asin = product.xpath('@data-asin').extract_first()
            product_url = f"https://www.amazon.com/dp/{asin}"
            yield scrapy.Request(url=product_url, callback=self.parse_product_page, meta={'asin': asin})
    
        # next_page = response.xpath('//li[@class="a-last"]/a/@href').extract_first()
        # if next_page:
        #     url = urljoin("https://www.amazon.com",next_page)
        #     yield scrapy.Request(url=product_url, callback=self.parse_keyword_response)

    def parse_product_page(self, response):
        asin = response.meta['asin']
        title = response.xpath('//*[@id="productTitle"]/text()').extract_first()
        #image = re.search('"large":"(.*?)"',response.text).groups()[0]
        rating = response.xpath('//*[@id="acrPopover"]/@title').extract_first()
        number_of_reviews = response.xpath('//*[@id="acrCustomerReviewText"]/text()').extract_first()
        bullet_points = response.xpath('//*[@id="feature-bullets"]//li/span/text()').extract()
        seller_rank = response.xpath('//*[text()="Amazon Best Sellers Rank:"]/parent::*//text()[not(parent::style)]').extract()

        price = response.xpath('//*[@id="priceblock_ourprice"]/text()').extract_first()

        if not price:
            price = response.xpath('//*[@data-asin-price]/@data-asin-price').extract_first() or \
                    response.xpath('//*[@id="price_inside_buybox"]/text()').extract_first()

        yield {'asin': asin, 'Title': title,'Rating': rating, 'NumberOfReviews': number_of_reviews,
               'Price': price,}
