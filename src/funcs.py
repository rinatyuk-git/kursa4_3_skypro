import json
from datetime import datetime

def upload_data(file_name):
    """
    загрузка json файла
    """
    with open(file_name, 'r') as file:  #открываем файл на чтение
        fin_info = json.load(file)      #загружаем из файла данные в словарь fin_info
    return fin_info                     #возвращаем полученный словарь

# print(upload_data('operations.json'))


def filtered_fin_info(fin_info: list[dict]) -> list[dict]:
    """
    очищаем и фильтруем полученный словарь
    """
    cleaned_info = list(filter(lambda n: len(n) and n['state'] == 'EXECUTED', fin_info))    # задаем параметры для фильтрации
    return cleaned_info     # выводим полученный результат

# print(filtered_fin_info(upload_data('operations.json')))


def sorted_fin_info(cleaned_info: list) -> list:
    """
    сортируем отфильтрованное инфо по дате и времени
    """
    sorts_fin_info = sorted(cleaned_info, key=lambda n: datetime.strptime(n['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True) # задаем требуемые параметры сортировки
    return sorts_fin_info # выводим полученную сортировку

# print(sorted_fin_info(filtered_fin_info(upload_data('operations.json'))))