
import sys


sys.path.append('C:\python')

import com.pythonizm.calc


print(com.pythonizm.calc.plus_value(1, 1))





# ======================== #
# 相対パスで指定してみる   #
# ======================== #

import calc as test

print(test.plus_value(10, 2))

# ↑ゲーム作る上では、多分こっちの方が重要度高い。しかも楽

