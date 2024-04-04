import os
from config import ROOT_DIR
# from pathlib import Path
from src.funcs import upload_data, filtered_fin_info, sorted_fin_info, changed_date_format, hidden_card_number, \
    get_amount, get_main

file = os.path.join(ROOT_DIR, 'src', 'operations.json')


def test_upload_data():
    assert upload_data(file)
