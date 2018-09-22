


import configparser

inifile = configparser.ConfigParser()
inifile.read('./config.ini', 'UTF-8')


print(inifile.get('ユーザー', 'name'))
print(inifile.get('ユーザー', 'name_kana'))
print(inifile.get('ユーザー', '備考'))


