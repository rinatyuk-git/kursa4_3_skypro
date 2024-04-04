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


def changed_date_format(date: str) -> str:
    """
    преобразование формата даты из полученной инфо в требуемый формат ДД.ММ.ГГГГ
    """
    # return f"{date[8:10]}.{date[5:7]}.{date[:4]}" # выводим требуемый формат
    good_time = datetime.strptime(date,'%Y-%m-%dT%H:%M:%S.%f')
    return good_time.strftime('%d.%m.%Y')  # выводим требуемый формат

# print(changed_date_format('2018-07-11T02:26:18.671407'))


def hidden_card_number(card):
    """
    создание маскировки по условию для карт в формате  XXXX XX** **** XXXX, для счета - **XXXX
    """
    num = card.split()  # разбивка строки с данными о платежной системе
    if num[0] == "Счет": # проверка на наличие слова Счет
        return f"Счет **{num[-1][-4:]}" # вывод замаскированного номера счета
    else:
        card_name = " ".join(num[:-1]) # сборка инфо о карте
        return f"{card_name} {num[-1][:4]} {num[-1][4:6]}** **** {num[-1][-4:]}" # вывод замаскированного номера карты

# print(hidden_card_number('Visa Classic 2842878893689012'))