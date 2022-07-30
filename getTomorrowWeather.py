import requests
from bs4 import BeautifulSoup


def get_html(url):
    if url == None:
        url = "https://www.tianqi.com/kaifuqu/"
    # header = { "cookie": "BAIDU_SSP_lcr=https://www.baidu.com/link?url=xnfTWDveqbLC-sHhfPP8llTCD-GrKz3n8IcutKj9e6s
    # -STeHh_DVdWy3Lgl-z71T&wd=&eqid=f65e8a5c00019c630000000662a2f7e7;
    # Hm_lvt_ab6a683aa97a52202eab5b3a9042a8d2=1654759452; Hm_lpvt_ab6a683aa97a52202eab5b3a9042a8d2=1654847644",
    # "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
    # Chrome/101.0.4951.67 Safari/537.36", ":authority": "www.tianqi.com", ":path": "/kaifuqu/mingtian/?qd=tq15",
    # "referer": "https://www.tianqi.com/kaifuqu/15/" } html = requests.get(url=url, headers=header)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE '
    }
    response_1 = requests.get(url, headers=headers)
    soup = BeautifulSoup(response_1.text, 'lxml')
    targetDiv = soup.find('div', class_='weatherbox')
    # 当前日期
    date = "今天是: " + targetDiv.find("dd", class_='week').text
    # 天气标签
    weathers = targetDiv.find("dd", class_="weather").find_all('b')
    # 空气质量
    kongqi = targetDiv.find("dd", class_="kongqi").contents[0].text + "  " + \
             targetDiv.find("dd", class_="kongqi").contents[2].text
    # 温度范围
    ranges = "今日温度: " + targetDiv.find("span").contents[1]
    # 当前温度
    nowTemperature = "当前温度: " + weathers[0].next + '℃'
    # 天气状况
    weatherCondition = "天气: " + weathers[1].next

    # 湿度
    shidu = targetDiv.find('dd', class_='shidu').contents[0].text
    # 风向
    fengxiang = targetDiv.find('dd', class_='shidu').contents[1].text
    # 紫外线
    ziwaixian = targetDiv.find('dd', class_='shidu').contents[2].text
    message = "<p>" + date + '</p><p>' + ranges + "</p><p>" + nowTemperature + "</p><p>" + weatherCondition + "</p><p>" + shidu + "</p><p>" + fengxiang + "</p><p>" + ziwaixian + "</p><p>" + kongqi + "</p>"
    # print(message)
    return message


if __name__ == '__main__':
    url = "https://www.tianqi.com/kaifuqu/"
    get_html(url)
