import scrapy
# we are going to parse the web page and dump the HTML on two html files

class QuotesSpider(scrapy.Spider):
    name = "quotes"        #identifies the spider, must be unique

    def start_requests(self): #where should the spider start crawling from?
        urls =  [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse) 

#callback function is parse

    def parse(self, response): #handles response for each reques
        page = response.url.split("/")[-2]
#page splits ULR by / and extracting the last 2 chars of the URL we are on
        filename = 'quotes-%s.html' % page
# % is the argument of which we pass a string
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
# spitting a log out to the terminal where we run the spider

