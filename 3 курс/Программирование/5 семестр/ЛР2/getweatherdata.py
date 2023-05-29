import requests
import json
# import key_openweather
import getweatherdata_test


def get_weather_data(place, api_key=''):
    req = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+ place + '&appid=' + api_key)
    if req.status_code == (400):
        print('Place-name issue')
        return None
    if req.status_code == (401):
        print('API key issue')
        return None
    res = json.loads(req.text)
    feels_like = round(res['main']['feels_like'] - 273.15, 2)
    if res['timezone'] < 0:
        timezone = 'UTC'+str(round(res['timezone'] / 3600))
    else:
        timezone = 'UTC+'+str(round(res['timezone'] / 3600))
    result = {"name": res['name'], "coord": res['coord'], "country": res['sys']['country'], "feels_like": feels_like, "timezone": timezone}
    return json.dumps(result)


if __name__ == "__main__":
    k = getweatherdata_test.key

    print(get_weather_data("Moscow", k))
    print(get_weather_data("Petersburg", k))
    print(get_weather_data("Dakka", k))