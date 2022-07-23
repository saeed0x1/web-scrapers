from email import header
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['imdb.com']
    # start_urls = ['https://www.imdb.com/search/title/?groups=top_250&sort=user_rating']
    
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'   

    def start_requests(self):
        yield scrapy.Request(url='https://www.imdb.com/search/title/?groups=top_250&sort=user_rating',headers={
            'User-Agent':self.user_agent
            })

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h3[@class='lister-item-header']/a"), callback='parse_item', follow=True,process_request='set_user_agent'),
        Rule(LinkExtractor(restrict_xpaths="//a[@class='lister-page-next next-page'][1]"),process_request='set_user_agent')
    )

    def set_user_agent(self,request,response):
        request.headers['User-Agent'] = self.user_agent
        return request


    def parse_item(self, response):
        yield{
            'title':response.xpath("//div[@class='sc-94726ce4-2 khmuXj']/h1/text()").get(),
            'year':response.xpath("//span[@class='sc-8c396aa2-2 itZqyK']/text()").get(),
            'duration':response.xpath("//li[@class='ipc-inline-list__item']/text()").getall(),
            'rating':response.xpath("//span[@class='sc-7ab21ed2-1 jGRxWM']/text()").get(),
            'movie_url':response.url,
            'user-agent':response.request.headers['User-Agent']
        }
 