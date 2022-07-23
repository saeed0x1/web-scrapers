from urllib.request import Request
import scrapy
import logging

class PopuPySpider(scrapy.Spider):
    name = 'popu'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']
    
    country_name = ''

    def parse(self, response):
        title = response.xpath("//h1/text()").get()
        countries = response.xpath("//td/a")

        for country in countries:
            name = country.xpath(".//text()").get()
            self.country_name = name
            link = country.xpath(".//@href").get()

            yield response.follow(url=link,callback=self.parse_country,meta={'country_name':name})

    def parse_country(self,response):
        name = response.request.meta['country_name']
        rows = response.xpath("//table[@class='table table-striped table-bordered table-hover table-condensed table-list']/tbody/tr")
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()
            
            yield{
                'country_name':name,
                'year':year,
                'populatie on':population
            }