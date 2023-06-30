def check_leap_year(year):
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        # print("閏年")
        return True, '閏年'
    else:
        # print("平年")
        return False, '平年'


year = int(input('請輸入年分'))
a, b = check_leap_year(year)
print(a, b)
