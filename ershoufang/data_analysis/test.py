import requests
from lxml import etree
import time
import csv
from selenium import webdriver

def csv_write(item):
    with open('./lagou00.csv', 'a', encoding='gbk', newline='') as csvfile:
        writer = csv.writer(csvfile)
        try:
            writer.writerow(item)
        except Exception as e:
            print('write error! ', e)


def spider():
    # r = requests.get(list_url, headers=headers, cookies=cookies)
    # time.sleep(4)
    # res = r.json()
    # print(res)
    driver.get('https://m.lagou.com/search.html')
    job_name = driver.find_element_by_xpath('//*[@placeholder="搜索公司或职位"]')
    job_name.send_keys('数据分析')
    submit = driver.find_element_by_xpath('//*[@class="search"]')
    submit.click()
    time.sleep(3)
    res = []
    for comp in res['content']['data']['page']['result']:
        com_url = 'http://m.lagou.com/jobs/' + str(comp['positionId']) + '.html'
        response = requests.get(com_url, headers=headers, cookies=cookies)
        time.sleep(6)
        sel = etree.HTML(response.text)
        try:
            nianxian = sel.xpath("//span[@class='item workyear']/span/text()")[0].strip()
        except:
            nianxian = ''
        try:
            xueli = sel.xpath("//span[@class='item education']/span/text()")[0].strip()
        except:
            xueli = ''
        try:
            zhize = sel.xpath("string(//div[@class='content'])").strip().replace('\xa0','')
        except:
            zhize = ''
        chengshi = comp['city']
        gongsi = comp['companyName']
        fabushijian = comp['createTime']
        zhiwei = comp['positionName']
        gongzi = comp['salary']
        item = [chengshi, gongsi, fabushijian, zhiwei, gongzi, xueli, nianxian, zhize]
        csv_write(item)
        print('正在抓取：', gongsi)

def coo_regular(cookie):
    coo = {}
    for k_v in cookie.split(';'):
        k, v = k_v.split('=', 1)
        coo[k.strip()] = v.replace('"', '')
        return coo


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = 'D:/soft/Python/Anaconda3/chromedriver.exe'

    # headers = {'Accept-Encoding': 'gzip, deflate', 'Connection': 'keep-alive', 'Host': 'm.lagou.com', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}
    # cookie = 'privacyPolicyPopup=false; PRE_UTM=; PRE_HOST=; PRE_LAND=https://www.lagou.com/; user_trace_token=20210516095318-d8ebf4cf-169b-4a49-886b-8bb0246a87d7; LGSID=20210516095318-c1b9fd99-06f5-4de7-8423-8a7c56d5c0a0; PRE_SITE=https://www.lagou.com; LGUID=20210516095318-ba075caa-187b-48da-ac0a-8fdc2e08d18d; _ga=GA1.2.2137850216.1621129999; sajssdk_2015_cross_new_user=1; sensorsdata2015session={}; sensorsdata2015jssdkcross={"distinct_id":"17972e0b531328-053bc9a81e6c68-d7e1739-1327104-17972e0b5328df","first_id":"","props":{"$latest_traffic_source_type":"直接流量","$latest_search_keyword":"未取到值_直接打开","$latest_referrer":"","$os":"Windows","$browser":"Chrome","$browser_version":"90.0.4430.93"},"$device_id":"17972e0b531328-053bc9a81e6c68-d7e1739-1327104-17972e0b5328df"}; index_location_city=全国; __lg_stoken__=aa043b6d3334ec1d9500316c273e88b15370d0d23595d59f9a4a86e5b0cd726b54d909a670e3a4286ff990120ca5f76080688f2962e870bf2d8874a40997dbc9899517094569; JSESSIONID=ABAAABAABGJABAJA1132F594A647F1776C8D7FA78AD76FF; _ga=GA1.3.2137850216.1621129999; X_HTTP_TOKEN=3d5badcc22dd501a2440311261fe7726eb0c3329cf; LGRID=20210516100042-857e065b-05ee-4719-a1b9-0825d84d8152'
    # cookies = coo_regular(cookie)
    # all_url = ['http://m.lagou.com/search.json?city=%E5%85%A8%E5%9B%BD&positionName=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&pageNo=' + str(x) + '&pageSize=15' for x in range(1, 180)]
    # for url in all_url:
    #     spider(url)
