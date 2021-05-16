from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ
phone_num = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)(\d{2})' \
            r'(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
phone_sub = r'+7(\4)\8-\11-\14\15\17\18\20'

new_contacts_list = list()
for keys in contacts_list:
    keys_string = ','.join(keys)
    result = re.sub(phone_num, phone_sub, keys_string)
    keys_as_list = result.split(',')
    new_contacts_list.append(keys_as_list)


full_name = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)' \
            r'(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
name_sub = r'\1\8\4\6\9\7\8'

new_contacts_list2 = list()
for keys in new_contacts_list:
    keys_string = ','.join(keys)
    result = re.sub(full_name, name_sub, keys_string)
    keys_as_list = result.split(',')
    new_contacts_list2.append(keys_as_list)

new_contacts_list3 = list()
for keys1 in new_contacts_list2:
    for keys2 in new_contacts_list2:
        if keys1[0] == keys2[0] and keys1[1] == keys2[1] and keys1 is not keys2:
            for i in range(len(new_contacts_list2[0])):
                    if keys1[i] == '':
                        keys1[i] = keys2[i]
        if len(keys1) > len(keys2) and keys1[-1] == "":
            keys1.pop()
for keys in new_contacts_list2:
    if keys not in new_contacts_list3:
        new_contacts_list3.append(keys)



# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook_new.csv", "w", newline="") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(new_contacts_list3)


