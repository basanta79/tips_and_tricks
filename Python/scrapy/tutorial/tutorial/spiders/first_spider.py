import scrapy


class FirstSpider(scrapy.Spider):

    name = 'first'

    def start_request(self):
        urls = ['http://www.2ionline.com',
                'http://2ionline.com']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print('##################################')
