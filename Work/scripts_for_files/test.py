import re

file = r'd:\Гордиен.txt'

open_file = open(file, 'r', encoding='utf-8')
read_file = open_file.read()
regex = re.compile('1c-docob')
read_file = regex.sub('docob', read_file)
regex = re.compile('1c-upkp')
read_file = regex.sub('upkp', read_file)
write_file = open(file, 'w', encoding='utf-8')
write_file.write(read_file)

























# import shutil
#
# paths = [
#     r'\\PC1874\c$\users\Ващенко\AppData\Roaming\1C\1CEStart\ibases.v8i',
#     r'\\PC1881\c$\users\Подмецкая\AppData\Roaming\1C\1CEStart\ibases.v8i',
#     r'\\PC1882\c$\users\Гордиенко_Е\AppData\Roaming\1C\1CEStart\ibases.v8i',
#     r'\\PC1884\c$\users\Пройдакова\AppData\Roaming\1C\1CEStart\ibases.v8i',
#     r'\\PC1886\c$\users\Шеховцова\AppData\Roaming\1C\1CEStart\ibases.v8i',
#     r'\\PC1887\c$\users\Шипилова\AppData\Roaming\1C\1CEStart\ibases.v8i',
# ]
#
#
# for file in paths:
#     shutil.copy(file, fr'D:/{file[18:25] + ".txt"}')
#     print('ok')
