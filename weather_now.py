import requests
from city_code import city_code

api = "https://weather.cma.cn/api/now/"


def get_weather(city):
    for key in city_code:
        if city == key:
            url = api + str(city_code[key])
            req = requests.get(url)
            data = req.json()
            # 地区
            loc = data['data']['location']['path']
            # 风向
            windDirection = data['data']['now']['windDirection']
            # 风向度
            windDirectionDegree = str(data['data']['now']['windDirectionDegree'])
            # 风速
            windSpeed = str(data['data']['now']['windSpeed'])
            # 风力等级
            windScale = str(data['data']['now']['windScale'])
            # 温度
            temperature = str(data['data']['now']['temperature'])
            # 气压
            pressure = str(data['data']['now']['pressure'])
            # 湿度
            humidity = str(data['data']['now']['humidity'])
            weather = {
                "地区": loc,
                "温度": temperature,
                "风向": windDirection,
                "风向度": windDirectionDegree,
                "风力等级": windScale,
                "风速": windSpeed,
                "湿度": humidity,
                "气压": pressure
            }
            return weather
        else:
            continue
    return 0
