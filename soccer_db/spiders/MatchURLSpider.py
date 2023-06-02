import scrapy
import pandas as pd

class MatchURLSpider(scrapy.Spider):
    name='match_url_spider'
    

    def start_requests(self):
        leagues=['https://www.skysports.com/premier-league-results','https://www.skysports.com/champions-league-results','https://www.skysports.com/fa-cup-results','https://www.skysports.com/europa-league-results','https://www.skysports.com/world-cup-results']
        urls=[]
        for l in leagues:
            for i in range(17,23):
                urls.append(l+'/20'+str(i)+'-'+str(i+1))
        for url in urls:
            yield scrapy.Request(url=url,callback=self.get_data)

    def get_data(self, response):
        url_list=response.xpath("//div[@class = 'fixres__item']/a/@href").extract()
        print('url lens'+str(len(url_list)))

        
        result_csv=pd.read_csv('/home/parsa/IUST/Spring_1402/NLP/Project/Phase1/soccer_db/data/row/data_sources.csv')
        new_row=pd.DataFrame({'url':url_list})
        result_csv=pd.concat([result_csv,new_row],ignore_index=True)
        result_csv=result_csv.loc[:,['url']]
        result_csv.to_csv('/home/parsa/IUST/Spring_1402/NLP/Project/Phase1/soccer_db/data/row/data_sources.csv')