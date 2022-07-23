import scrapy


class TinySpider(scrapy.Spider):
    name = 'tiny'
    allowed_domains = ['www.tinydeals.co']
    start_urls = ['https://www.tinydeals.co/']

    def parse(self, response):

        prod_name = response.xpath("//h2[@class='woocommerce-loop-product__title']/text()").getall()
        prod_price = response.xpath("//span[@class='price']/span/bdi/text()").getall()
        for product in response.xpath("//a[@class='woocommerce-LoopProduct-link woocommerce-loop-product__link']"):
            yield{
                'product_name ':product.xpath(".//woocommerce-loop-product__title/text()").get(),
                'product_price':product.xpath(".//")
            }
