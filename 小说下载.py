#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
if __name__ == "__main__":
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }
    #url = 'http://www.sanguoxs.net/sanguoyanyi/'
    url = 'https://www.7017k.com/wanmeishijie/'
    page_text = requests.get(url=url,headers=headers).text
    #在首页中解析出章节的标题和详情页的url
    #print(page_text)
    #1,实例化BeautifulSoup对象，需要将页面源码数据加载到该页面当中
    soup = BeautifulSoup(page_text,'lxml')
    #解析章节标题和详情页的url
    dd_list = soup.select('.listmain > dl > dd' )
    fp = open('./完美世界.txt','w',encoding='utf-8')
    for dd in dd_list:
        title = dd.a.string
        #print(title)
        detail_url = 'https://www.7017k.com/'+dd.a['href']
        #print(detail_url)
        #对详情页发起请求，解析出章节内容
        detail_page_text = requests.get(url=detail_url,headers=headers).text
        #解析出详情页中相关的章节内容
        detail_soup = BeautifulSoup(detail_page_text,'lxml')
        div_tag = detail_soup.find('div',class_= 'showtxt')
        #解析到了章节的内容
        content = div_tag.text
        fp.write(title+':'+content+'\n')
        print(title,'爬取成功！！！')

