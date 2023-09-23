'''
requests 爬取墨迹天气福州15天天气数据
bs4 解析获取的信息
格式化返回所有天气信息
'''
#导入所需包
import requests
import bs4
import time

#网址
url = 'https://tianqi.moji.com/forecast15/china/fujian/fuzhou'

#返回值与源代码
response = requests.get(url)
html = response.text

#定义一个soup
soup = bs4.BeautifulSoup(html,'html.parser')

#使用bs4解析网页源代码
span_week = soup.findAll('span', attrs={'class': 'week'})
div_temp1 = soup.findAll('b')
div_temp2 = soup.findAll('strong')
span_wea = soup.findAll('span', attrs={'class': 'wea'})
div_temp3 = soup.findAll('div',attrs={'class': 'detail_ware_title'})
div_time = soup.findAll('div',attrs={'class': 'detail_time clearfix'})

#为后面的日期与天气设置可控索引
weekx = 0
weeky = 1

#天气预报内容
print('\t    福州市15天天气预报')
for t in div_time:
    print(f"\t今日日期: {t.text[0:11]}")

print('=' * 40)

#天气预报内容格式化返回
for i1,i2 in zip(div_temp1[1:], div_temp2[2:]):
    try:

        print(f"| 日期: {span_week[weekx].text} {span_week[weeky].text}")
        print(f"| 最高气温: {i1.text}")
        print(f"| 最低气温: {i2.text}")
        if span_wea[weekx].text == span_wea[weeky].text:
            print(f"| 天气: {span_wea[weekx].text}\n|{'=' * 40}")
        else:
            print(f"| 天气: {span_wea[weekx].text} 转 {span_wea[weeky].text}\n|{'=' * 40}")
        weekx += 2
        weeky += 2
        #等待0.5秒，防止对方服务器负担
        time.sleep(0.5)
        
    #防止出现找不到索引错误
    except IndexError:
        pass
    
#穿衣建议格式化返回
for i3 in div_temp3:
    print(f"\t{i3.text}")
    print('=' * 60)
print('|\t\t\t祝您生活愉快!\t\t\t   |')

print('=' * 60)

#随意按一个键退出
input()