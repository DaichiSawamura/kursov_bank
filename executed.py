import json
import requests
import datetime
from datetime import datetime


def data_filter():
    """фильтрует данные по executed"""
    raw_data = requests.get("https://www.jsonkeeper.com/b/IDU8").json()
    filter_data = []
    for i in raw_data:
        if not (i.get('from') and i.get('state')):
            continue
        if i['state'] == 'EXECUTED':
            date = datetime.strptime(i['date'], '%Y-%m-%dT%H:%M:%S.%f')
            date = date.strftime('%Y.%m.%d')
            filter_data.append(
                {'date': date, 'description': i['description'], 'from': i['from'], 'to': i['to'],
                 'operationAmount': i['operationAmount']
                 }
            )
    return filter_data
