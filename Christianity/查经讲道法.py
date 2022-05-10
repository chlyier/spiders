# -*- coding:utf-8 -*-


import requests
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

text = '<p><a target="_blank" href="http://mp.weixin.qq.com/s?__biz=MzUzNjcwNzc4Ng==&amp;mid=2247486184&amp;idx=1&amp;sn=e92db827d16d996c761ac169235c640f&amp;chksm=faf35d4dcd84d45b92c47c01687a2a4a0dd9e5ed06329736ebbf227d14c3a0d6e7f1303c3a64&amp;scene=21#wechat_redirect" data-itemshowtype="0" tab="innerlink" data-linktype="2">第1课-基本功</a><br  /></p><p><a target="_blank" href="http://mp.weixin.qq.com/s?__biz=MzUzNjcwNzc4Ng==&amp;mid=2247486295&amp;idx=1&amp;sn=9d3f27757d91fb7528dcababb14e270f&amp;chksm=faf35cf2cd84d5e443abcab69c45c84959d8bdeaefa930509221de177a1c01b1de79a7c81c6e&amp;scene=21#wechat_redirect" data-itemshowtype="0" tab="innerlink" data-linktype="2">第2课-传道能力的来源</a><br  /></p><p><a target="_blank" href="http://mp.weixin.qq.com/s?__biz=MzUzNjcwNzc4Ng==&amp;mid=2247486935&amp;idx=3&amp;sn=6401020d717c9a025ed174099316d288&amp;chksm=faf35a72cd84d364bc02c73e32a356399cd52be5cabadc2106e068739e73ab9e377166ec5c1b&amp;scene=21#wechat_redirect" data-itemshowtype="0" tab="innerlink" data-linktype="2">第3课-组织讲章的四个要素</a><br  /></p><p><a target="_blank" href="http://mp.weixin.qq.com/s?__biz=MzUzNjcwNzc4Ng==&amp;mid=2247486935&amp;idx=4&amp;sn=aa1a7ceae3f073ceeae134add5c59782&amp;chksm=faf35a72cd84d36436c061698ec1e0bbcbb5ba8cdf51525484dc2f100d0917b65890db498c77&amp;scene=21#wechat_redirect" data-itemshowtype="0" tab="innerlink" data-linktype="2">第4课-组织讲章的两种方法</a><br  /></p><p><a target="_blank" href="http://mp.weixin.qq.com/s?__biz=MzUzNjcwNzc4Ng==&amp;mid=2247486964&amp;idx=2&amp;sn=4535b2f98ba65bd487a16095d6ab9f66&amp;chksm=faf35a51cd84d347b235d7ebe95b4ab747dbfec4b7f8d775d08ca262c1e741fc99c9485a7c3b&amp;scene=21#wechat_redirect" data-itemshowtype="0" tab="innerlink" data-linktype="2">第5课-真理的项目</a><br  /></p><p><a target="_blank" href="http://mp.weixin.qq.com/s?__biz=MzUzNjcwNzc4Ng==&amp;mid=2247487127&amp;idx=2&amp;sn=23cd514d9595fc4997ff6dfd15c7b0d6&amp;chksm=faf35932cd84d0245eaab0126fa66299ae785bf94b768fd7a8d5d452b63d78804e9faa75b484&amp;scene=21#wechat_redirect" data-itemshowtype="0" tab="innerlink" data-linktype="2">第6课-聆听的重要</a><br  /></p><p><a target="_blank" href="http://mp.weixin.qq.com/s?__biz=MzUzNjcwNzc4Ng==&amp;mid=2247487207&amp;idx=3&amp;sn=6dad02fb4e0f1a7fe5c7d96ca20b3a4a&amp;chksm=faf35942cd84d05429a70ca93c8a96bc68d82720380c115f313ff45521944df4a03a80ffe38d&amp;scene=21#wechat_redirect" data-itemshowtype="0" tab="innerlink" data-linktype="2">第7课-以经解经</a><br  /></p><p><a target="_blank" href="http://mp.weixin.qq.com/s?__biz=MzUzNjcwNzc4Ng==&amp;mid=2247487342&amp;idx=3&amp;sn=bf1968bc04d6076246b52459fe93e75d&amp;chksm=faf358cbcd84d1ddbf37116fa430ad4838197f5d14393ad255209d302dc2ddd5a0bd3e879724&amp;scene=21#wechat_redirect" data-itemshowtype="0" tab="innerlink" data-linktype="2">第8课-灵性的预备</a><br  /></p><p><a target="_blank" href="http://mp.weixin.qq.com/s?__biz=MzUzNjcwNzc4Ng==&amp;mid=2247487495&amp;idx=5&amp;sn=1adc21a57283e3177931793dcae0185e&amp;chksm=faf347a2cd84ceb4328c5f886836a3795d6deca15e2827c5fbd2e008f37c5c88b4e7f97fca8b&amp;scene=21#wechat_redirect" data-itemshowtype="0" tab="innerlink" data-linktype="2">第9课-默想的重要</a><br  /></p><p><a target="_blank" href="http://mp.weixin.qq.com/s?__biz=MzUzNjcwNzc4Ng==&amp;mid=2247487538&amp;idx=3&amp;sn=9cdb1357c8c0eec8476c1ac449a533f0&amp;chksm=faf34797cd84ce817c8ed24f67e088ff8c40911350169ee5cad294d4f21d3389f50c2c4566a8&amp;scene=21#wechat_redirect" data-itemshowtype="0" tab="innerlink" data-linktype="2">第10课-分卷研究的必要</a><br  /></p><p><a target="_blank" href="http://mp.weixin.qq.com/s?__biz=MzUzNjcwNzc4Ng==&amp;mid=2247487562&amp;idx=2&amp;sn=093e03ac21c36c4c111f0dae02cd34fd&amp;chksm=faf347efcd84cef965a0872ac228d3b1919484f40da40d1e1316ddfcfacb90d9e236fc5d9ed4&amp;scene=21#wechat_redirect" data-itemshowtype="0" tab="innerlink" data-linktype="2">第11课-一个定律</a><br  /></p><p><a target="_blank" href="http://mp.weixin.qq.com/s?__biz=MzUzNjcwNzc4Ng==&amp;mid=2247487611&amp;idx=3&amp;sn=d823ec0be400e65f72d85a208a5ec8ea&amp;chksm=faf347decd84cec8f0301dec3b43a5d0b2c3d301a50d0c744dd06e795567d4f5e35b22743314&amp;scene=21#wechat_redirect" data-itemshowtype="0" tab="innerlink" data-linktype="2">第12课-圣言的大能</a><br  /></p><p><a target="_blank" href="http://mp.weixin.qq.com/s?__biz=MzUzNjcwNzc4Ng==&amp;mid=2247487631&amp;idx=3&amp;sn=5a4587240c202791adf5a4b0d82091df&amp;chksm=faf3472acd84ce3ce59ab02ccfc640c0d996157d9fdcc8d70e4920027fad636753567f6285bc&amp;scene=21#wechat_redirect" data-itemshowtype="0" tab="innerlink" data-linktype="2">第13课-瓦典西人的榜样</a><br  /></p><p><a target="_blank" href="http://mp.weixin.qq.com/s?__biz=MzUzNjcwNzc4Ng==&amp;mid=2247487650&amp;idx=4&amp;sn=059f72d6b93f867a61c088e01dbcdc2f&amp;chksm=faf34707cd84ce117528c2e65c8fe88f069c07fdd55ee553de2eea1d1e5e92cb7425ff6b388d&amp;scene=21#wechat_redirect" data-itemshowtype="0" tab="innerlink" data-linktype="2">第14课-隐藏的脉络</a><br  /></p>'

browser = webdriver.Edge('msedgedriver.exe')

def download_audio(page_link, title):
    for i in range(0, 33):
        browser.get(page_link[i])
        time.sleep(1)
        btn = browser.find_elements(By.XPATH, '//*[@id="audio_play_btn"]')
        for a in btn:
            a.click()
        time.sleep(2)
        html = browser.page_source
        ex = 'autoplay="" src="(.*?)"'
        audio_link = re.findall(ex, html, re.S)

        index = 0
        for link in audio_link:
            data = requests.get(link, timeout=20).content
            path = 'D:/zz/查经讲道法/' + str(i+1) + title[i] + str(index) + '.mp3'
            with open(path, 'wb') as fp:
                fp.write(data)
                print(id, '下载成功')
                index += 1

if __name__ == '__main__':
    page_link = []
    ex = '<p><a target="_blank" href="(.*?)"'
    page_link += re.findall(ex, text, re.S)

    title = []
    ex1 = 'data-linktype="2">(.*?)</a><br  /></p>'
    title += re.findall(ex1, text, re.S)

    # print(len(page_link))
    # print(len(title))

    download_audio(page_link, title)