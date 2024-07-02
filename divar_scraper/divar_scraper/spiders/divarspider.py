import scrapy

class DivarSpider(scrapy.Spider):
    name = "divarspider"
    allowed_domains = ["divar.ir"]
    start_urls = ["https://divar.ir/s/tehran"]

    def parse(self, response):
        # Corrected CSS selector with a dot for class
        posts = response.css('title::text').get()
        yield {
            'title': posts
        }

