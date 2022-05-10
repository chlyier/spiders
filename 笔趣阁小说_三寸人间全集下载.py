import requests
import re  # 系统内置

import io
import sys
# #改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')


def download_one(src, title):
    base_url = 'http://www.xbiquge.la'+src
    response_one = requests.get(base_url)
    response_one.encoding = response_one.apparent_encoding
    html_one = response_one.text

    # 获取小说文本  解析数据时，一切数据以终端为准
    base_text = re.findall('<div id="content">(.*?)<p><a href="http://koubei.baidu.com/s/xbiquge.la" target="_blank">亲,点击进去,给个好评呗,分数越高更新越快,据说给新笔趣阁打满分的最后都找到了漂亮的老婆哦!</a><br />手机站全新改版升级地址：http://m.xbiquge.la，数据和书签与电脑站同步，无广告清新阅读！</p></div>', html_one, re.S)[0]
    text = base_text.replace('&nbsp;', ' ').replace('<br />', '\n')
    with open(title + '.txt', 'w', encoding='utf-8') as fp: 
        fp.write(text)
    

url = 'http://www.xbiquge.la/10/10489/'  # 总页面，静态页面
response = requests.get(url)
response.encoding = response.apparent_encoding  # 自动识别响应体的编码
html = response.text  # 首页源代码

# 数据解析，获取所有链接
result_list = re.findall("<dd><a href='(.*?)' >(.*?)</a>.*</dd>", html) # ()表示精确匹配  .表示匹配除了换行符之外的任意字符  *匹配前一个字符的0次或者多次  ？表示非贪婪模式

for src, title in result_list:
    download_one(src, title)

