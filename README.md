# weather-forecast-mojiwea

代码是一个用于爬取墨迹天气福州15天天气数据
并格式化输出的Python程序。这个程序的主要功能包括：
使用requests库发送HTTP请求，
获取墨迹天气福州的网页源代码。
使用BeautifulSoup库解析网页源代码，
提取所需的天气信息，包括日期、最高气温、最低气温和天气状况。
将提取的天气信息进行格式化输出，
包括每日的日期、最高气温、最低气温和天气状况，
并在不同日期之间使用分隔线进行分隔。
输出穿衣建议，将其格式化为带有分隔线的形式。
添加了等待时间，以防止对方服务器过度负担。
最后，程序等待用户按下任意键后退出。

并且，感谢墨迹天气
