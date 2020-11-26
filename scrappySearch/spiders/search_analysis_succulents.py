import scrapy


class SearchAnalysisSucculentsSpider(scrapy.Spider):
    name = 'search_analysis_succulents'
    allowed_domains = ['https://www.succulentsandsunshine.com/blog/']
    start_urls = ['http://https://www.succulentsandsunshine.com/blog//']

    def parse(self, response):
        pass
