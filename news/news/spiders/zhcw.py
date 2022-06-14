import scrapy


class ZhcwSpider(scrapy.Spider):
    # 爬虫的名字  
    name = 'zhcw'
    # 允许访问的域名
    allowed_domains = ['zhwc.com']
    # 起始url地址
    start_urls = ['http://zhwc.com/']

    def parse(self, response):
        pass
