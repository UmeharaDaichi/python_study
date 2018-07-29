
title = ' 文字列の桁揃え(埋め文字指定の「rjust」)'
print(title.rjust(25, '◇'))



test_str = '1234'

print(test_str.rjust(10, '0'))
print(test_str.rjust(10, '!'))


print('\n')
title = '\n◇ ゼロ埋めの「zfill」'
print(title.zfill(40))

print(test_str.zfill(10))
print(test_str.zfill(3))