'''
Created on 2016年10月25日

@author: sun
'''

from yb import url_manager
from yb import html_downloader
from yb import html_parser
from yb import html_outputer

class SpiderMain(object):
    def _init_(self):
        self.urls=url_manager.UrlManager();
        self.downloader=html_downloader.HtmlDownloader();
        self.parser=html_parser.HtmlParser();
        self.outputer=html_outputer.HtmlOutputer();
    
    def craw(self, root_url):
        count=1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url=self.urls.get_new_url()
                print 'craw %d:%s'%(count,new_url)
                html_cont=self.downloader.download(new_url)
                new_urls,new_data=self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_url)
                self.outputer.collect_data(new_data)
            
                if count==1:
                    break
            
                count=count+1
            except:
                print 'craw failed'
                
        self.outputer.output_html()



if _name_=="_main_":
    root_url="https://www.yuanbao.com/news/?corpid=0"
    obj_spider=SpiderMain()
    obj_spider.craw(root_url)