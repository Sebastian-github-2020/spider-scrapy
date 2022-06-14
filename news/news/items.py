# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass



"""
项目名称
	项目名字
		spider文件夹 存储爬虫文件
				init
		init
		items  定义数据结构 爬虫抓取数据的数据模型
		middleware  中间件 代理
		pipelines 管道  处理下载的数据
		settings 配置文件  robots协议  us定义等(user-agent)
		
		

"""
