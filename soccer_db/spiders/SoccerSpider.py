import scrapy
import pandas as pd

class SoccerSpider(scrapy.Spider):
    name='soccer_spider'
    def start_requests(self):
        urls=pd.read_csv('/home/parsa/IUST/Spring_1402/NLP/Project/Phase1/soccer_db/data/row/data_sources.csv')
        urls=urls['url']
        for url in urls:
            yield scrapy.Request(url=url,callback=self.get_data)

    def get_data(self, response):
        try:
            report_list=response.xpath("//div[@class = 'sdc-article-body sdc-article-body--lead']/p/text()").extract()
            rating_list=response.xpath("//p[@class = 'sdc-article-factbox__text']/text()").extract()
            ratings=''
            report=''
            for r in report_list:
                report+=str(r)
            
            for r in rating_list:
                ratings+=str(r)

            
            result_csv=pd.read_csv('/home/parsa/IUST/Spring_1402/NLP/Project/Phase1/soccer_db/data/row/result.csv')
            new_row=pd.DataFrame({'report':[report] , 'ratings':[ratings]})
            result_csv=pd.concat([result_csv,new_row],ignore_index=True)
            result_csv=result_csv.loc[:,['report','ratings']]
            result_csv.to_csv('/home/parsa/IUST/Spring_1402/NLP/Project/Phase1/soccer_db/data/row/result.csv')
        except:
            print('This page cannot be used')