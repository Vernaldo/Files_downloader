import scrapy
from ..items import FiledownloaderItem

class FileSpider(scrapy.Spider):
    name = 'files'
    start_urls = ['https://tubidy.mobi/search.php?q=Marshmello']

    def parse(self, response):
        items = FiledownloaderItem()
        all_files = response.css('.col-xs-12')
    
        for files in all_files:
            file_name = files.css('.media-heading::text').extract()
            file_duration = files.css('.pagecontent , .video-search-footer li:nth-child(1)::text').extract()
            if file_name is not None:
                yield response.follow(file_name, callback = self.initial_options)

            def initial_options(self,response):
                file_type_option = response.css('body > div.container-fluid.pagecontent > div > div > div > div > div.row.donwload-box > ul > li:nth-child(3) > a').css('#donwload_box > ul > li:nth-child(3) > a')
                yield{response}
    
    
            items['file_name'] =  file_name,
            items['file_duration'] =  file_duration,
                 

            yield items
        
        next_page = response.css('li.next a::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)




