import os
from config import ROOT_DIR
# from pathlib import Path
from src.funcs import upload_data, filtered_fin_info, sorted_fin_info, changed_date_format, hidden_card_number, \
    get_amount, get_main

file = os.path.join(ROOT_DIR, 'src', 'operations.json')


def test_upload_data():
    assert upload_data(file)


def test_filtered_fin_info():
    cor_inputs = [{"state": "EXECUTED"}]
    empty_inputs = [{}]
    noncor_inputs = [{"state": "CANCELED"}]
    assert filtered_fin_info(cor_inputs) == cor_inputs
    assert filtered_fin_info(empty_inputs) == []
    assert filtered_fin_info(noncor_inputs) == []


def test_sorted_fin_info():
    corr_date = [{"date": "2019-12-08T22:46:21.935582"}, {"date": "2018-07-11T02:26:18.671407"}]
    assert sorted_fin_info(corr_date) == corr_date


def test_changed_date_format():
    assert changed_date_format('2018-07-11T02:26:18.671407') == '11.07.2018'


def test_hidden_card_number():
    assert hidden_card_number('Счет 72082042523231456215') == 'Счет **6215'
    assert hidden_card_number('Visa Platinum 8990922113665229') == 'Visa Platinum 8990 92** **** 5229'


