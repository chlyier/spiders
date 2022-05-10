import re
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def download_audio(url_list):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'}

    i = 1
    for url in url_list:
        data = requests.get(url=url, headers=header, timeout=20).content
        path = 'D:/zz/没有治不了的病/第' + str(i) + '节.mp3'
        with open(path, 'wb') as fp:
            fp.write(data)
            print(i, '下载成功')
        i = i + 1


def get_page_link():
    url = 'https://mp.weixin.qq.com/s/rUuut92I6AEHUGyBU_wcWQ'
    html = requests.get(url).text
    # print(html)

    list = []
    ex = '<a href="(.*?)" target="_blank"'
    list += re.findall(ex, html, re.S)
    print(list)
    print(len(list))

    return list

def get_audio_link(url_list):
    browser = webdriver.Edge('msedgedriver.exe')
    audio_link = []

    for url in url_list:
        url = url.replace('\/', '/')

        browser.get(url)
        time.sleep(1)
        btn = browser.find_element(By.XPATH, '//*[@id="audio_play_btn"]')
        btn.click()
        time.sleep(2)
        html = browser.page_source
        ex = 'autoplay="" src="(.*?)"'
        audio_link += re.findall(ex, html, re.S)

    print(audio_link)
    print(len(audio_link))

    return audio_link

if __name__ == "__main__":
    # page_list = get_page_link()

    # 由上面的得到下面的page_list
    # page_list = ['https://mp.weixin.qq.com/s?__biz=MzI4MzM0MTE2NA==&amp;mid=2247486836&amp;idx=1&amp;sn=aa4895cca4140aa0c97f8917851c7493&amp;scene=21#wechat_redirect', 'https://mp.weixin.qq.com/s?__biz=MzI4MzM0MTE2NA==&amp;mid=2247488059&amp;idx=1&amp;sn=f18c623869b16cba95cd69b8eea4d170&amp;scene=21#wechat_redirect', 'https://mp.weixin.qq.com/s?__biz=MzI4MzM0MTE2NA==&amp;mid=2247486927&amp;idx=1&amp;sn=f266c5018e974893fbd1a168beda04dd&amp;scene=21#wechat_redirect', 'https://mp.weixin.qq.com/s?__biz=MzI4MzM0MTE2NA==&amp;mid=2247487965&amp;idx=1&amp;sn=cb785882949494ac7dba46f192bcbde7&amp;scene=21#wechat_redirect', 'https://mp.weixin.qq.com/s?__biz=MzI4MzM0MTE2NA==&amp;mid=2247487615&amp;idx=1&amp;sn=297bb38011290bd333e5beb9e014982c&amp;scene=21#wechat_redirect', 'https://mp.weixin.qq.com/s?__biz=MzI4MzM0MTE2NA==&amp;mid=2247487977&amp;idx=2&amp;sn=cb02c4ea238a6e1487d3d8a3546bf5a9&amp;scene=21#wechat_redirect', 'https://mp.weixin.qq.com/s?__biz=MzI4MzM0MTE2NA==&amp;mid=2247487988&amp;idx=1&amp;sn=7a997fd3962350dcce5a7c7492bf6af0&amp;scene=21#wechat_redirect', 'https://mp.weixin.qq.com/s?__biz=MzI4MzM0MTE2NA==&amp;mid=2247487655&amp;idx=1&amp;sn=347ec4465f97f0c5f285bf05ad0db09e&amp;scene=21#wechat_redirect', 'https://mp.weixin.qq.com/s?__biz=MzI4MzM0MTE2NA==&amp;mid=2247487995&amp;idx=1&amp;sn=5d4426a41cdd5fb238c37d41e65efdcb&amp;scene=21#wechat_redirect', 'https://mp.weixin.qq.com/s?__biz=MzI4MzM0MTE2NA==&amp;mid=2247487995&amp;idx=2&amp;sn=a71e6db9ac3ff66b388fb4b8776ffe1c&amp;scene=21#wechat_redirect', 'https://mp.weixin.qq.com/s?__biz=MzI4MzM0MTE2NA==&amp;mid=2247487648&amp;idx=1&amp;sn=2935ba8e8a47387541fb62cfe0e51bb7&amp;scene=21#wechat_redirect', 'https://mp.weixin.qq.com/s?__biz=MzI4MzM0MTE2NA==&amp;mid=2247486965&amp;idx=1&amp;sn=db6200136d9e80f5b647991cc3206825&amp;scene=21#wechat_redirect', 'https://mp.weixin.qq.com/s?__biz=MzI4MzM0MTE2NA==&amp;mid=2247486978&amp;idx=1&amp;sn=536457e15263fbe191dcba2d80504892&amp;scene=21#wechat_redirect', 'https://mp.weixin.qq.com/s?__biz=MzI4MzM0MTE2NA==&amp;mid=2247487035&amp;idx=1&amp;sn=e1c9b3766c8d95442fd97760c7e4b0c7&amp;scene=21#wechat_redirect', 'https://mp.weixin.qq.com/s?__biz=MzI4MzM0MTE2NA==&amp;mid=2247487061&amp;idx=1&amp;sn=7c18d0b1bc980192fb3fb283e77e3134&amp;scene=21#wechat_redirect', 'https://mp.weixin.qq.com/s?__biz=MzI4MzM0MTE2NA==&amp;mid=2247487069&amp;idx=1&amp;sn=e4379250c4e59f394895eb958fee59d5&amp;scene=21#wechat_redirect', 'https://mp.weixin.qq.com/s?__biz=MzI4MzM0MTE2NA==&amp;mid=2247487126&amp;idx=1&amp;sn=eda02cbe5ff1ff884d2a88f9a45f9fe9&amp;scene=21#wechat_redirect', 'https://mp.weixin.qq.com/s?__biz=MzI4MzM0MTE2NA==&amp;mid=2247487202&amp;idx=1&amp;sn=1869f91318ab5d5ed1bbbefce318b8ad&amp;scene=21#wechat_redirect', 'https://mp.weixin.qq.com/s?__biz=MzI4MzM0MTE2NA==&amp;mid=2247487381&amp;idx=1&amp;sn=791aa37b6a2bcb2964beefdfcb962cd1&amp;scene=21#wechat_redirect', 'https://mp.weixin.qq.com/s?__biz=MzI4MzM0MTE2NA==&amp;mid=2247487385&amp;idx=1&amp;sn=1c5ca87fa5111a41387303596a2f8c63&amp;scene=21#wechat_redirect', 'https://mp.weixin.qq.com/s?__biz=MzI4MzM0MTE2NA==&amp;mid=2247487454&amp;idx=1&amp;sn=c5582d3c0708a3e6001216648acf2c5d&amp;scene=21#wechat_redirect', 'https://mp.weixin.qq.com/s?__biz=MzI4MzM0MTE2NA==&amp;mid=2247487458&amp;idx=1&amp;sn=042912b950709204265c6b7559b8ed88&amp;scene=21#wechat_redirect', 'https://mp.weixin.qq.com/s?__biz=MzI4MzM0MTE2NA==&amp;mid=2247487462&amp;idx=1&amp;sn=5c83e9e969dfa0504ba304b7b3477be3&amp;scene=21#wechat_redirect', 'https://mp.weixin.qq.com/s?__biz=MzI4MzM0MTE2NA==&amp;mid=2247487466&amp;idx=1&amp;sn=a3a36217a582609a2897e80cf6b75e4a&amp;scene=21#wechat_redirect', 'https://mp.weixin.qq.com/s?__biz=MzI4MzM0MTE2NA==&amp;mid=2247487470&amp;idx=1&amp;sn=5b75b3854b6034db8ee28f2cfd0f3135&amp;scene=21#wechat_redirect', 'https://mp.weixin.qq.com/s?__biz=MzI4MzM0MTE2NA==&amp;mid=2247488059&amp;idx=2&amp;sn=6ec5a5f53bc3a7b4542658f933f4810a&amp;scene=21#wechat_redirect', 'https://mp.weixin.qq.com/s?__biz=MzI4MzM0MTE2NA==&amp;mid=2247487485&amp;idx=1&amp;sn=2b666f349f596f4d1b2504a8d7b4bc20&amp;scene=21#wechat_redirect', 'https://mp.weixin.qq.com/s?__biz=MzI4MzM0MTE2NA==&amp;mid=2247484079&amp;idx=3&amp;sn=4171e9cb3902f514ab914b1b885480d1&amp;scene=21#wechat_redirect', 'https://mp.weixin.qq.com/s?__biz=MzI4MzM0MTE2NA==&amp;mid=2247484079&amp;idx=2&amp;sn=484f607696c4897dd7953325bf5a2bb0&amp;scene=21#wechat_redirect', 'https://mp.weixin.qq.com/s?__biz=MzI4MzM0MTE2NA==&amp;mid=2247485502&amp;idx=1&amp;sn=d3bc1a05beccdc6a53c1f08b546aa6cb&amp;scene=21#wechat_redirect', 'https://mp.weixin.qq.com/s?__biz=MzI4MzM0MTE2NA==&amp;mid=2247484496&amp;idx=1&amp;sn=c01a2f29cfae12d1dcabccb3bfa6da5a&amp;scene=21#wechat_redirect', 'https://mp.weixin.qq.com/s?__biz=MzI4MzM0MTE2NA==&amp;mid=2247484505&amp;idx=1&amp;sn=28d250ed6c16de401f030c5151b76869&amp;scene=21#wechat_redirect', 'https://mp.weixin.qq.com/s?__biz=MzI4MzM0MTE2NA==&amp;mid=2247484492&amp;idx=1&amp;sn=4b7349aef9e770ec5f1fdf90b2dc7ae6&amp;scene=21#wechat_redirect']
    # for i in range(0, len(page_list) - 6):
    #     print(page_list[i])

    # audio_link = get_audio_link(page_list)

    # 由上面两个得到下面的audio_link
    audio_link = ['https://res.wx.qq.com/voice/getvoice?mediaid=MzI4MzM0MTE2NF8yMjQ3NDg2ODM1', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI4MzM0MTE2NF8yMjQ3NDg4MDU3', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI4MzM0MTE2NF8yMjQ3NDg2OTI2', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI4MzM0MTE2NF8yMjQ3NDg3OTY0', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI4MzM0MTE2NF8yMjQ3NDg3NjE0', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI4MzM0MTE2NF8yMjQ3NDg3OTc2', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI4MzM0MTE2NF8yMjQ3NDg3OTg1', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI4MzM0MTE2NF8yMjQ3NDg3NjU0', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI4MzM0MTE2NF8yMjQ3NDg3OTkz', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI4MzM0MTE2NF8yMjQ3NDg3OTk0', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI4MzM0MTE2NF8yMjQ3NDg3NjQ3', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI4MzM0MTE2NF8yMjQ3NDg2OTY0', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI4MzM0MTE2NF8yMjQ3NDg2OTc3', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI4MzM0MTE2NF8yMjQ3NDg3MDM0', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI4MzM0MTE2NF8yMjQ3NDg3MDYw', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI4MzM0MTE2NF8yMjQ3NDg3MDY4', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI4MzM0MTE2NF8yMjQ3NDg3MTI1', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI4MzM0MTE2NF8yMjQ3NDg3MjAx', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI4MzM0MTE2NF8yMjQ3NDg3Mzgw', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI4MzM0MTE2NF8yMjQ3NDg3Mzg0', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI4MzM0MTE2NF8yMjQ3NDg3NDUz', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI4MzM0MTE2NF8yMjQ3NDg3NDU3', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI4MzM0MTE2NF8yMjQ3NDg3NDYx', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI4MzM0MTE2NF8yMjQ3NDg3NDY1', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI4MzM0MTE2NF8yMjQ3NDg3NDY5', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI4MzM0MTE2NF8yMjQ3NDg4MDU4', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI4MzM0MTE2NF8yMjQ3NDg3NDg0', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI4MzM0MTE2NF8yMjQ3NDg0MDc4', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI4MzM0MTE2NF8yMjQ3NDg1NTAx', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI4MzM0MTE2NF8yMjQ3NDg0NDk1', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI4MzM0MTE2NF8yMjQ3NDg0NTA0', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI4MzM0MTE2NF8yMjQ3NDg0NDkx']

    # print(audio_link)
    # print(len(audio_link))

    download_audio(audio_link)
