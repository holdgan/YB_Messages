'''
Created on 2016年10月25日

@author: sun
'''
if _name_=="_main_":
    root_url="https://www.yuanbao.com/news/?corpid=0"
    obj_spider=SpiderMain()
    obj_spider.craw(root_url)