import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        books = response.css('article.product_pod')
        for i in books:
            yield {
            'name': i.css('h3 a::text').get(),
            'price': i.css('.product_price .price_color::text').get(),
            'url': i.css('h3 a').attrib['href']
            }
