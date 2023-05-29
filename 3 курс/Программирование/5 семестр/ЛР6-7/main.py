"""
Разработать фрагмент программы, позволяющий получать данные о текущих курсах валют с сайта Центробанка РФ с использованием сервиса, который они предоставляют. Применить шаблон проектирования «Одиночка» для предотвращения отправки избыточных запросов к серверу ЦБ РФ (запретить вызов функции get_currencies более 1 раза в секунду). Оформить решение в виде корректно работающего приложения, реализовать тестирование и опубликовать его в портфолио.
Страница документации: https://cbr.ru/development/
"""

# http://www.cbr.ru/scripts/XML_daily.asp
import requests
import time
from xml.etree import ElementTree as ET

class TooManyRequests(Exception):
    pass

  
def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return getinstance


@singleton
class CurrenciesList():
    def __init__(self):
        self.latest_req_time = 0

    def get_currencies(self, currencies_ids_lst=None):
        req_time = time.time()

        if req_time - self.latest_req_time < 1:
            raise TooManyRequests('one function call per second is allowed')

        self.latest_req_time = req_time

        if currencies_ids_lst is None:
            currencies_ids_lst = [
                'R01239', 'R01235', 'R01035', 'R01815', 'R01585F', 'R01589',
                'R01625', 'R01670', 'R01700J', 'R01710A'
            ]

        cur_res_str = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')

        result = {}

        # XML Tree
        root = ET.fromstring(cur_res_str.content)

        valutes = root.findall("Valute")

        for _v in valutes:
            valute_id = _v.get('ID')

            if str(valute_id) in currencies_ids_lst:
                valute_cur_val = _v.find('Value').text
                valute_cur_name = _v.find('Name').text

                result[valute_id] = (valute_cur_val, valute_cur_name)

        return result

if __name__ =='__main__':
    l1 = CurrenciesList()
    res = l1.get_currencies(["R01090B", "R01720", "R01565"])
    print(res)

    # time.sleep(1.0)

    l2 = CurrenciesList()
    res = l2.get_currencies(["R01090B", "R01720", "R01565"])
    print(res)