import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"        #identifies the spider, must be unique

    def start_requests(self): #where should the spider start crawling from?
        urls =  [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response): #handles response for each reques
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
