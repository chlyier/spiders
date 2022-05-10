import requests
import parsel
import io
import sys
# #改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
    'Referer': 'https://www.ximalaya.com/youshengshu/16411402/'
}


# 下载一个音频
def download_one_music(song_id, name):
    # api_url只是一个变量（接口url），利用api_url获得音频链接
    api_url = 'https://www.ximalaya.com/revision/play/v1/audio?id='+song_id+'&ptype=1'
    response = requests.get(api_url, headers=headers)
    src = response.json()['data']['src']  # 获得音频链接
    print(src)

    """下载音频"""
    # 请求单个音频，请求的是音频，没有text属性，所以直接打印看一下
    response = requests.get(src, headers=headers)

    # 图片，视频，音频，pdf文件都是二进制的，二进制没有编码，文本有编码，文本要用encoding='utf-8'
    with open(name + '.m4a', 'wb') as fp:
        fp.write(response.content)


# 下载一个页面的30个音频
def download_one_page(page_url):
    response = requests.get(page_url, headers=headers)
    html = response.text
    selector = parsel.Selector(html)

    lis = selector.css('li._Vc')
    for li in lis:
        title = li.css('div.text._Vc a::attr(title)').get()
        href = li.css('div.text._Vc a::attr(href)').get()
        song_id = href.split('/')[-1]
        print(song_id, title)
        download_one_music(song_id, title)


# 下载所有40页的音频
base_page_url = 'https://www.ximalaya.com/youshengshu/16411402/p{}/'
for i in range(1, 41):
    print(base_page_url.format(i))
    download_one_page(base_page_url.format(i))