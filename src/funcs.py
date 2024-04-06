import json
from datetime import datetime

def upload_data(file_name):
    """
    загрузка json файла
    """
    # открываем файл на чтение
    with open(file_name, 'r') as file:
        # загружаем из файла данные в словарь fin_info
        fin_info = json.load(file)
    # возвращаем полученный словарь
    return fin_info

# print(upload_data('operations.json'))


def filtered_fin_info(fin_info: list[dict]) -> list[dict]:
    """
    очищаем и фильтруем полученный словарь
    """
    # задаем параметры для фильтрации
    cleaned_info = list(filter(lambda n: len(n) and n['state'] == 'EXECUTED', fin_info))
    # выводим полученный результат
    return cleaned_info

# print(filtered_fin_info(upload_data('operations.json')))


def sorted_fin_info(cleaned_info: list) -> list:
    """
    сортируем отфильтрованное инфо по дате и времени
    """
    # задаем требуемые параметры сортировки
    sorts_fin_info = sorted(cleaned_info, key=lambda n: datetime.strptime(n['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)
    # выводим полученную сортировку
    return sorts_fin_info

# print(sorted_fin_info(filtered_fin_info(upload_data('operations.json'))))


def changed_date_format(date: str) -> str:
    """
    преобразование формата даты из полученной инфо в требуемый формат ДД.ММ.ГГГГ
    """
    # return f"{date[8:10]}.{date[5:7]}.{date[:4]}" # выводим требуемый формат
    # получаем инфо о дате в исходном формате
    good_time = datetime.strptime(date,'%Y-%m-%dT%H:%M:%S.%f')
    # выводим требуемый формат
    return good_time.strftime('%d.%m.%Y')

# print(changed_date_format('2018-07-11T02:26:18.671407'))


def hidden_card_number(card: str) -> str:
    """
    создание маскировки по условию для карт в формате  XXXX XX** **** XXXX, для счета - **XXXX
    """
    # разбивка строки с данными о платежной системе
    num = card.split()
    # проверка на наличие слова Счет
    if num[0] == "Счет":
        # вывод замаскированного номера счета
        return f"Счет **{num[-1][-4:]}"
    else:
        # сборка инфо о карте
        card_name = " ".join(num[:-1])
        # вывод замаскированного номера карты
        return f"{card_name} {num[-1][:4]} {num[-1][4:6]}** **** {num[-1][-4:]}"

# print(hidden_card_number('Visa Classic 2842878893689012'))


def get_amount(money: str) -> str:
    """
    выводим сумму, включая наименование валюты
    """
    # задаем структуру вывода суммы и валюты
    return f'{money["operationAmount"]["amount"]} {money["operationAmount"]["currency"]["name"]}'

# print(get_amount({
#     "operationAmount": {
#       "amount": "73778.48",
#       "currency": {
#         "name": "руб.",
#         "code": "RUB"
#       }}}))


def get_main(file, oper_loop=5):
    """
    собираем все воедино - функция вывода репорта
    """
    # c = sorted_fin_info(filtered_fin_info(upload_data(file)))
    fin_info = upload_data(file)
    filter_fin_info = filtered_fin_info(fin_info)
    sort_fin_info = sorted_fin_info(filter_fin_info)
    result = []

    for i in sort_fin_info:
        if oper_loop == 0:
            break
        output_data = []
        # собираем строку вида: Дата Наименование платежа
        output_data.append(" ".join([changed_date_format(i['date']), i['description']]))
        responder = []
        # проверка наличие фразы: "Открытие вклада"
        if i['description'] != "Открытие вклада":
            # собираем строку вида: Отправитель платежа ->
            responder.append(hidden_card_number(i['from']) + ' ->')
        # собираем строку вида: Получатель платежа
        responder.append(hidden_card_number(i['to']))
        # собираем все строки, содеражащие текст
        output_data.append(" ".join(responder))
        # выводим сумму, включая валюту
        output_data.append(get_amount(i))
        # задаем счетчик
        oper_loop -= 1
        # создаем финальный аид репорта
        result.append(output_data)
    # выводим репорт
    return result

# get_main('operations.json')