from typing import List
from mathstats import MathStats

FILE = 'Retail.csv'
FILE2 = 'MarketingSpend.csv'

def main():
    default_file = FILE
    data = read_data(default_file)
    choice1 = int(
        input(
            f"По умолчанию выбран файл {default_file} . Выберите функцию:\n1. Посчитать количество различных invoices\n2. Посчитать различные значения любого из полей\n3. Показать общее количество запрашиваемого товара\n4. Сменить файл на MarketingSpend.csv\n"
              ))
    if choice1 == 1:
        print(
              "Укажите, с какого среза данных хотите посчитать invoices в формате '№_строки_начала №_строки конца'. Если хотите считать все строки, введите '0 0'"
              )
        start, end = 0, 0
        try:
            start, end = (int(c) for c in input() if c != ' ')
        except ValueError:
            print("Номера строк введены некорректно.")
        if start == 0 and end == 0:
            print(
                  f"Уникальных invoices во всём файле: {count_invoice(data)}"
                  )
        elif (start > 0) and (end > 0):
            print(
                  f"Уникальных invoices в строках с {start}-й по {end}-ю: {count_invoice(data[start:end])}"
                  )
        else:
            print("Номера строк введены некорректно.")
    elif choice1 == 2:
        key = ""
        available_fields = list(data[0].keys())
        print(
              f"Укажите название поля. Доступные поля:\n{available_fields}"
                )
        key = str(input())
        if key in available_fields:
            print(
                  f"Подсчёт уникальных {key} во всём файле:\n{count_different_values(data, key)}"
                  )
        else:
            print("Поле не найдено.")
          
    elif choice1 == 3:
      stock_code = int(input("Введите stock code: "))
      print(f"Общее количество товара {stock_code}: {get_total_quantity(data, stock_code)}")
      
    elif choice1 == 4:
        default_file = FILE2
        stats = MathStats(default_file)
        print(f"Среднее: {stats.get_mean}\nМаксимум: {stats.max}\nМинимум: {stats.min}\nДисперсия: {stats.disp}\nСреднее квадратичное: {stats.sigma_sq}")
    print('-' * 10)
    """
        data2 = MathStats(FILE2)
        slice_test1 = data2.data[:2]
    
        print(data2.get_mean(slice_test1))  # (4500.0, 2952.43)
    """


def read_data(file: str) -> List[dict]:
    # считывание данных и возвращение значений в виде списка из словарей
    import csv
    data = []
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for _r in reader:
            row = {
                'InvoiceNo': int(_r['InvoiceNo']),
                'InvoiceDate': _r['InvoiceDate'],
                'StockCode': int(_r['StockCode']),
                'Quantity': int(_r['Quantity'])
            }
            data.append(row)
    return data


def count_invoice(data: List[dict]) -> int:
    count = 0
    from collections import Counter
    # Реализуем получение номер invoices и помещение их в список
    # Переписать через генератор списка (done)
    invoices = [_el['InvoiceNo'] for _el in data]

    count = len(Counter(invoices))
    return count


def count_different_values(data: List[dict], key: str) -> int:
    """
    Функция должна возвращать число различных значений для столбца key      в списке data
    key - InvoiceNo или InvoiceDate или StockCode
    (done)
    """
    from collections import Counter
    count = 0
    invoices = [_el[key] for _el in data]
    count = len(Counter(invoices))
    return count


def get_total_quantity(data: List[dict], stock_code: int) -> int:
    """
    Возвращает общее количество проданного товара для данного stock_code
  (done)
    """
    result = 0
    for _el in data:
        if _el['StockCode'] == stock_code:
            result += _el['Quantity']
    return result


if __name__ == "__main__":
    main()
