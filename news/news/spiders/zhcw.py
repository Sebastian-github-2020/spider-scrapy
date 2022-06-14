import scrapy
from scrapy.http import Response


class ZhcwSpider(scrapy.Spider):
    # 爬虫的名字
    name = 'zhcw'
    # 允许访问的域名
    allowed_domains = ['zhwc.com']
    # 起始url地址
    start_urls = ['http://zhwc.com/']

    def parse(self, response: Response):
        """
        运行了 起始url后执行的方法
        :param response: 请求返回的数据  (未处理的数据) 获取的详情结果
        :return:
        """
        s = response.xpath("//ul[@class='asdas']")
