from change_numbers import raw_list
from change_numbers import hide_numbers_to
from change_numbers import hide_numbers_from

list_from = hide_numbers_from()
list_to = hide_numbers_to()


for i in range(len(raw_list)):
    print(f"{raw_list[i]['date']} {raw_list[i]['description']}")
    print(f"{list_from[i]}-> {list_to[i]}")
    print(f"{raw_list[i]['operationAmount']['amount']} {raw_list[i]['operationAmount']['currency']['name']}\n")

