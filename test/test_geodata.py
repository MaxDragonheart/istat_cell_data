from pathlib import Path

import pandas as pd

from istatcelldata.census2021.config import REGIONS_ROOT, REGIONS_COLUMN, PROVINCES_ROOT, PROVINCES_COLUMN, \
    PROVINCES_COLUMN_REMAPPING, MUNICIPALITIES_ROOT, MUNICIPALITIES_COLUMN
from istatcelldata.geodata import read_administrative_boundaries

main_folder = Path("/home/max/Desktop/census/preprocessing")

def test_read_regions(tmp_path: Path):
    print("test_read_major_boundaries")
    data = read_administrative_boundaries(
        file_path=main_folder.joinpath(*REGIONS_ROOT),
        target_columns=REGIONS_COLUMN,
        index_column=REGIONS_COLUMN[0],
        with_geometry=True,
        output_folder=tmp_path,
        layer_name='test'
    )
    print(data)
    assert isinstance(data, pd.DataFrame) or isinstance(data, Path)


def test_read_provinces():
    print("test_read_major_boundaries")
    data = read_administrative_boundaries(
        file_path=main_folder.joinpath(*PROVINCES_ROOT),
        target_columns=PROVINCES_COLUMN,
        index_column=PROVINCES_COLUMN[0],
        column_remapping=PROVINCES_COLUMN_REMAPPING
    )
    print(data)
    assert isinstance(data, pd.DataFrame)


def test_read_municipalities():
    print("test_read_major_boundaries")
    data = read_administrative_boundaries(
        file_path=main_folder.joinpath(*MUNICIPALITIES_ROOT),
        target_columns=MUNICIPALITIES_COLUMN,
        index_column=MUNICIPALITIES_COLUMN[0]
    )
    print(data)
    assert isinstance(data, pd.DataFrame)
