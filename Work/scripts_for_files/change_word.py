#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import shutil

paths = [
    r'\\PC1805\c$\users\Акутина\AppData\Roaming\1C\1CEStart\ibases.v8i',
    r'\\PC1806\c$\users\Шапошникова\AppData\Roaming\1C\1CEStart\ibases.v8i',
    r'\\PC1813\c$\users\Жучкова\AppData\Roaming\1C\1CEStart\ibases.v8i',
    r'\\PC1822\c$\users\Комарова\AppData\Roaming\1C\1CEStart\ibases.v8i',
    r'\\PC1827\c$\users\Ганус\AppData\Roaming\1C\1CEStart\ibases.v8i',
    r'\\PC1844\c$\users\Пичугова\AppData\Roaming\1C\1CEStart\ibases.v8i',
    r'\\PC1847\c$\users\Гергерт\AppData\Roaming\1C\1CEStart\ibases.v8i',
    r'\\PC1849\c$\users\Артеменко\AppData\Roaming\1C\1CEStart\ibases.v8i',
    r'\\PC1850\c$\users\Райшуотене\AppData\Roaming\1C\1CEStart\ibases.v8i',
    r'\\PC1852\c$\users\Слюсарева\AppData\Roaming\1C\1CEStart\ibases.v8i',
    r'\\PC1853\c$\users\Григоренко\AppData\Roaming\1C\1CEStart\ibases.v8i',
    r'\\PC1854\c$\users\Жемчужен\AppData\Roaming\1C\1CEStart\ibases.v8i',
    r'\\PC1855\c$\users\Биянов\AppData\Roaming\1C\1CEStart\ibases.v8i',
    r'\\PC1856\c$\users\Хвостов\AppData\Roaming\1C\1CEStart\ibases.v8i',
    r'\\PC1857\c$\users\Рыбинская\AppData\Roaming\1C\1CEStart\ibases.v8i',
    r'\\PC1858\c$\users\Долгих\AppData\Roaming\1C\1CEStart\ibases.v8i',
    r'\\PC1859\c$\users\Миколаенко\AppData\Roaming\1C\1CEStart\ibases.v8i',
    r'\\PC1862\c$\users\Гулевич\AppData\Roaming\1C\1CEStart\ibases.v8i',
    r'\\PC1863\c$\users\Каныгина\AppData\Roaming\1C\1CEStart\ibases.v8i',
    r'\\PC1867\c$\users\Белова\AppData\Roaming\1C\1CEStart\ibases.v8i',
    r'\\PC1871\c$\users\Гаврикова\AppData\Roaming\1C\1CEStart\ibases.v8i',
    r'\\PC1874\c$\users\Ващенко\AppData\Roaming\1C\1CEStart\ibases.v8i',
    r'\\PC1881\c$\users\Подмецкая\AppData\Roaming\1C\1CEStart\ibases.v8i',
    r'\\PC1882\c$\users\Гордиенко_Е\AppData\Roaming\1C\1CEStart\ibases.v8i',
    r'\\PC1883\c$\users\Стороженко\AppData\Roaming\1C\1CEStart\ibases.v8i',
    r'\\PC1884\c$\users\Пройдакова\AppData\Roaming\1C\1CEStart\ibases.v8i',
    r'\\PC1885\c$\users\Александрова\AppData\Roaming\1C\1CEStart\ibases.v8i',
    r'\\PC1886\c$\users\Шеховцова\AppData\Roaming\1C\1CEStart\ibases.v8i',
    r'\\PC1887\c$\users\Шипилова\AppData\Roaming\1C\1CEStart\ibases.v8i',
    r'\\PC2008\c$\users\Зубанова\AppData\Roaming\1C\1CEStart\ibases.v8i',
    r'\\PC2058\c$\users\Никипорец\AppData\Roaming\1C\1CEStart\ibases.v8i',
    r'\\PC2061\c$\users\Белиба\AppData\Roaming\1C\1CEStart\ibases.v8i',
    r'\\PC2062\c$\users\Даниленко\AppData\Roaming\1C\1CEStart\ibases.v8i',
    r'\\PC2232\c$\users\Мироненко_Ю\AppData\Roaming\1C\1CEStart\ibases.v8i',
    r'\\PC2233\c$\users\Редкозубова\AppData\Roaming\1C\1CEStart\ibases.v8i'
]

ping = ''
codir = ''

for file in paths:
    try:
        print(file)
        open_file = open(file, 'r', encoding='utf-8')
        read_file = open_file.read()
        regex = re.compile('1c-docob')
        read_file = regex.sub('docob', read_file)
        regex = re.compile('1c-upkp')
        read_file = regex.sub('upkp', read_file)
        write_file = open(file, 'w', encoding='utf-8')
        write_file.write(read_file)
    except OSError:
        # print('Неправильное имя пользователя или не пингуется', end='\n''\n')
        ping += file + "      "
        file = file.partition('\A')[0]
        file1 = file[2:8] + " " + file[18:]
        ping += file1 + "\n"
        continue


    print('finished', end='\n''\n')

print('Компы, которые не пингуются')
print(ping, end='\n''\n')
