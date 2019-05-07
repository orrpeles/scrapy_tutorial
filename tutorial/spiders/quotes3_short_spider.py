#!/bin/python

import scrapy
class QuotesSpider(scrapy.Spider):
    name="quotes3_short"
    start_urls = [
            'http://quotes.toscrape.com/page/1/'
            ]
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css("span.text::text").get(),
                'author': quote.css("small.author::text").get(),
                }
            
        for href in response.css('li.next a'):    
            yield response.follow(href, callback=self.parse)
 
# ref: https://docs.scrapy.org/en/latest/intro/tutorial.html#a-shortcut-for-creating-requests



