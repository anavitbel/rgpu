import getweatherdata as w
import getweatherdata_test

k = getweatherdata_test.key
print(w.get_weather_data("Moscow", k))
print(w.get_weather_data("Petersburg", k))
print(w.get_weather_data("Dakka", k))