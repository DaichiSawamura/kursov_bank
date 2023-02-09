import datetime
from executed import data_filter


class Date:

    def __init__(self, title="", date=datetime.datetime.now()):
        self.title = title
        self.date = date

    def __repr__(self):
        return f"Date({self.title}, {self.date}"

    def name(self):
        return self.title


def date_filter():
    """сортирует список по дате"""
    raw_list = data_filter()
    filter_list = []
    for i in range(len(raw_list)):
        filter_list.append(Date(title=raw_list[i], date=(raw_list[i]['date'])))
    filter_list.sort(key=lambda name: name.date, reverse=True)
    return filter_list


def last_five():
    """берёт из списка последние 5 операций"""
    raw_list = date_filter()
    raw_last_five_list = []
    last_five_list = []
    for i in range(5):
        raw_last_five_list.append(raw_list[i])
    for x in range(5):
        last_five_list.append(Date.name(raw_last_five_list[x]))
    return last_five_list


