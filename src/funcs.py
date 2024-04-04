import json


def upload_data(file_name):
    """
    загрузка json файла
    """
    with open(file_name, 'r') as file:  #открываем файл на чтение
        fin_info = json.load(file)      #загружаем из файла данные в словарь fin_info
    return fin_info                     #возвращаем полученный словарь

# print(upload_data('operations.json'))
