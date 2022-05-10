# -*- coding:utf-8 -*-

import re
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

info = [{'title': '第廿二题  但以理最后三章的异象（五）但11-30-45──罗马教廷和末次南北王的争战', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486993&amp;amp;idx=4&amp;amp;sn=3c92fa1ba08c5cb23b75dcdcbe9c8ea3&amp;amp;chksm=fcca7955cbbdf04391a3b96cbd73697c931934041126a55a5a50ba38d735babd8109d0496e07&amp;amp;scene=21#wechat_redirect'}, {'title': '第廿二题  但以理最后三章的异象（五）但11-30-45──罗马教廷和末次南北王的争战', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486993&amp;amp;idx=5&amp;amp;sn=6dab4d20b09f2adba47bd13e851ace3d&amp;amp;chksm=fcca7955cbbdf0439ec67abf46811ad87b1d7d7381178e8de045939612cf6b66d4fb56a5bacc&amp;amp;scene=21#wechat_redirect'}, {'title': '第廿二题  但以理最后三章的异象（五）但11-30-45──罗马教廷和末次南北王的争战', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486993&amp;amp;idx=6&amp;amp;sn=c361edb518e37a2454865a9941225a0f&amp;amp;chksm=fcca7955cbbdf0431598c5aa200194dfa4097025045e8080fcbf8e955560842ccef8dd1e9615&amp;amp;scene=21#wechat_redirect'}, {'title': '第廿二题  但以理最后三章的异象（五）但11-30-45──罗马教廷和末次南北王的争战', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247486993&amp;amp;idx=7&amp;amp;sn=2ce173cf843cdfc54daac81e132640e3&amp;amp;chksm=fcca7955cbbdf0435c7d77bd4057c04c2fe9d1c006c8c71c4bfbb78aa046bb5d85fcc8967bff&amp;amp;scene=21#wechat_redirect'}, {'title': '第廿三题  但以理最后三章的异象（六）但以理第十二章预言', 'url': 'http://mp.weixin.qq.com/s?__biz=MzU3MjgwOTc3MQ==&amp;amp;mid=2247485819&amp;amp;idx=1&amp;amp;sn=ec25d30815bc0c1c57ca4e4859cd3d59&amp;amp;chksm=fcca7e3fcbbdf7294254f74ae3073b281343c73cc337714af91b4ee91ffce8482cc6ea0683f0&amp;amp;scene=21#wechat_redirect'}]

browser = webdriver.Edge('msedgedriver.exe')


def download_audio(id, m_dict):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'}

    index = 1
    for i in m_dict['audio_link']:
        data = requests.get(url=i, headers=header, timeout=20).content
        path = 'D:/zz/路光圣道/但以理研究与默想/' + str(id) + m_dict['title'] + str(index) + '.mp3'
        with open(path, 'wb') as fp:
            fp.write(data)
            print(id, '下载成功')
        index = index + 1


def get_audio_link(i):
    browser.get(i['url'])
    time.sleep(1)
    btn = browser.find_elements(By.XPATH, '//*[@id="audio_play_btn"]')
    for a in btn:
        a.click()
    time.sleep(2)
    html = browser.page_source
    ex = 'autoplay="" src="(.*?)"'
    audio_link = re.findall(ex, html, re.S)

    m_dict = {}
    m_dict['title'] = i['title']
    m_dict['audio_link'] = audio_link

    return m_dict


if __name__ == "__main__":
    id = 30
    for i in info:
        name_audio_dict = get_audio_link(i)
        print(name_audio_dict)
        download_audio(id, name_audio_dict)
        id = id + 1
