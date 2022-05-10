from selenium import webdriver
import time

# 搜索商品
def search_product(key):
    driver.find_element_by_xpath('//*[@id="q"]').send_keys(key)
    driver.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button').click()
    driver.maximize_window()
    time.sleep(10)  # 用于登陆淘宝

# 解析数据
def get_product():
    divs = driver.find_elements_by_xpath('//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')
    for div in divs:
        info = div.find_element_by_xpath('.//div[@class="row row-2 title"]/a').text  # 商品名称
        price = div.find_element_by_xpath('.//strong').text + '元'  # 商品的价格
        deal = div.find_element_by_xpath('.//div[@class="deal-cnt"]').text  # 商品的销量
        shop_name = div.find_element_by_xpath('.//div[@class="shop"]/a').text  # 店铺名称
        print(info, price, deal, shop_name, sep='||')

# 主入口
def main():
    search_product('u盘')
    get_product()

if __name__ == "__main__":
    # keyword = input("请输入你要搜索的商品关键字：")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.taobao.com')
    time.sleep(3)
    main()