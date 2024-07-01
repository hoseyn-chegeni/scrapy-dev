import scrapy


class DivarpiderSpider(scrapy.Spider):
    name = "divarpider"
    allowed_domains = ["divar.ir"]
    start_urls = ["https://divar.ir"]

    def parse(self, response):
        pass
