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
        path = 'D:/zz/健康新起点/第' + str(i) + '节.mp3'
        with open(path, 'wb') as fp:
            fp.write(data)
            print(i, '下载成功')
        i = i + 1


def get_page_link():
    url = 'https://mp.weixin.qq.com/s?__biz=MzI0NzEyMzgxMg==&mid=2653215735&idx=1&sn=e22b8d57b7d19c907910a7fb9b6e3603&chksm=f264a1fcc51328ea5bd93ef7eefa27f1b55ab7fd9fdce441a557fc26b29829570c23b6cce4fc&scene=178&cur_album_id=1480544160637059076#rd'
    html = requests.get(url).text
    # print(html)

    list = []
    ex = '<a target="_blank" href="(.*?)"'
    list += re.findall(ex, html, re.S)
    # print(url_list)

    return list

def get_audio_link(url_list):
    browser = webdriver.Edge('msedgedriver.exe')
    audio_link = []

    for url in url_list:
        url = url.replace('\/', '/')

        browser.get(url)
        time.sleep(1)
        btn = browser.find_element(By.XPATH, '//*[@id="voice_play"]')
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
    # audio_link = get_audio_link(page_list)

    # 由上面两个得到下面的audio_link
    audio_link = ['https://res.wx.qq.com/voice/getvoice?mediaid=MzI0NzEyMzgxMl8yNjUzMjE1NjYx', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI0NzEyMzgxMl8yNjUzMjE1NjYy', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI0NzEyMzgxMl8yNjUzMjE1NjYz', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI0NzEyMzgxMl8yNjUzMjE1NjY0', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI0NzEyMzgxMl8yNjUzMjE1NjY1', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI0NzEyMzgxMl8yNjUzMjE1NjY2', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI0NzEyMzgxMl8yNjUzMjE1NjY3', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI0NzEyMzgxMl8yNjUzMjE1NjY4', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI0NzEyMzgxMl8yNjUzMjE1Njcx', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI0NzEyMzgxMl8yNjUzMjE1Njgx', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI0NzEyMzgxMl8yNjUzMjE1Njcz', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI0NzEyMzgxMl8yNjUzMjE1Njgz', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI0NzEyMzgxMl8yNjUzMjE1Njg0', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI0NzEyMzgxMl8yNjUzMjE1Njg1', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI0NzEyMzgxMl8yNjUzMjE1Njg2', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI0NzEyMzgxMl8yNjUzMjE1Njg3', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI0NzEyMzgxMl8yNjUzMjE1Njg4', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI0NzEyMzgxMl8yNjUzMjE1Njkx', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI0NzEyMzgxMl8yNjUzMjE1Njky', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI0NzEyMzgxMl8yNjUzMjE1Njkz', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI0NzEyMzgxMl8yNjUzMjE1Njk0', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI0NzEyMzgxMl8yNjUzMjE1Njk1', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI0NzEyMzgxMl8yNjUzMjE1Njk2', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI0NzEyMzgxMl8yNjUzMjE1Njk3', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI0NzEyMzgxMl8yNjUzMjE1Njk4', 'https://res.wx.qq.com/voice/getvoice?mediaid=MzI0NzEyMzgxMl8yNjUzMjE1NzAx']
    print(audio_link)
    print(len(audio_link))

    download_audio(audio_link)
