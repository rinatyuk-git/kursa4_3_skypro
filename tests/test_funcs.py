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