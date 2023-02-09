from date import last_five

raw_list = last_five()


def hide_numbers_to():
    '''шифрует цифры переводов куда'''
    raw_list_to = []
    list_to = []
    for i in raw_list:
        x = i['to']
        raw_list_to.append(x)
    for y in raw_list_to:
        if 'Счет' in y:
            list_to.append(f'Счет **{y[-4:]}')
        else:
            list_to.append(f'{y[:-16]}{y[-16:-12]} {y[-11:-9]}** **** {y[-4:]} ')
    return list_to


def hide_numbers_from():
    '''шифрует цифры переводов откуда'''
    raw_list_from = []
    list_from = []
    for i in raw_list:
        x = i['from']
        raw_list_from.append(x)
    for y in raw_list_from:
        if 'Счет' in y:
            list_from.append(f'Счет **{y[-4:]}')
        else:
            list_from.append(f'{y[:-16]}{y[-16:-12]} {y[-11:-9]}** **** {y[-4:]} ')
    return list_from
