import scrapy


class DosiSpider(scrapy.Spider):

    name = 'first_scrapy'
    start_urls = ['http://2ionline.com']

    def parse(self, response):
        yield {'title': response}
