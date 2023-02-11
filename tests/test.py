from date import last_five
from change_numbers import hide_numbers_to
from change_numbers import hide_numbers_from
from executed import data_filter


def test_last_five():
    assert len(last_five()) == 5


def test_hide_numbers_to():
    assert "*" or "**" in hide_numbers_to()


def test_hide_numbers_from():
    assert "*" or "**" in hide_numbers_from()


def test_data_filter():
    assert data_filter() != []
