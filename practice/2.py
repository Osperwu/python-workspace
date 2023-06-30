'''
如果 i 是奇數，輸出 Odd；如果 i 是偶數，則輸出 Even。
'''
from unicodedata import decimal

try:
    n = decimal(input('只能輸入數字'))
    if (n % 2 == 0):
        print('odd、偶數',n % 2)
    else:
        print('even、基數',n % 2)
except TypeError as e:
    print('type')
    print(e)
except ValueError as e:
    print('輸入錯誤')
    # raise e
except Exception as e:
    print(e)
    print('大錯誤')
