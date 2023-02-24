from pathlib import Path

from census_istat.data.manage_data import read_csv, merge_data
from test.generic import csv_data

test_path = Path('/home/max/Desktop/census_istat/preprocessing/census_1991/data')


def test_read_csv(tmp_path: Path):
    print('test_read_csv')
    read_csv(csv_path=csv_data)


def test_merge_data(tmp_path: Path):
    print('test_merge_data')
    merge_data(
        csv_path=test_path,
        year=1991,
        output_path=tmp_path
    )

