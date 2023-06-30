# Note: 眼尖的你可能發現， statement 前方有四個空格，
# 這個動作叫縮排(indentation)。
# 在 Python 中要去判斷「哪些程式碼屬於某層級之下」不是使用大括號 {} 
# ，而是使用縮排判斷，只要在同一層縮排就是屬於上方「:」下的內容。
# 因此縮排在 Python 中是十分重要的，而根據 Python的協定 PEP8 的規定，
# 在 Python 中我們會使用「四個空格」來縮排。

"""
test1
"""
# score = int(input("請輸入成績"))
# if score >= 60:
#     print("成績及格!")
# elif score-5 <= 20:
#     print('留級')
# else :
#     print('補考')

    
"""
test2
"""
ID = input('輸入年紀')
year = int(ID[1:3])
print(year)
if year < 4:
    print("Graduated")
elif year <= 7 and year >= 4:
    if year == 7:
        print("Freshman")
    elif year == 6:
        print("Sophomore")
    elif year == 5:
        print("Junior")
    elif year == 4:
        print("Senior")
else:
    print("Not Registered Yet")