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
        pass
    
    



if _name_=="_main_":
    root_url="https://www.yuanbao.com/news/?corpid=0"
    obj_spider=SpiderMain()
    obj_spider.craw(root_url)