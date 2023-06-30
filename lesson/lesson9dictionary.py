'''
tuple(1,2,3)
list[4,5,6,6,6...]
set {7,8,9}
dictionary{key1: value1, key2: value2}
'''
movie = {'name': 'Saving Private Ryan',  # 電影名稱
         'year': 1998,  # 電影上映年份
         'director': 'Steven Spielberg',  # 導演
         'Writer': 'Robert Rodat',  # 編劇
         'Stars': ['Tom Hanks', 'Matt Damon', 'Tom Sizemore'],  # 明星
         'Oscar ': ['Best Director', 'Best Cinematography', 'Best Sound', 'Best Film Editing',
                    'Best Effects, Sound Effects Editing']
         # 獲得的奧斯卡獎項
         }
print(type(movie))
print(movie['director'])
print('**********************************')
movie_1 = {'name': 'Saving Private Ryan',
           'year': 1998,
           'director': 'Steven Spielberg'}
movie_2 = dict(name='The Breakfast Club',
               year=1985,
               director='John Hughes')
movie_3 = {'name': 'Catch Me If You Can',
           'year': 2002,
           'director': 'Steven Spielberg'}

print(movie_3['director'])  # 執行後會得到 Steven Spielberg
# print(movie_1["cast"])  # 這個會回傳錯誤的訊息
print(movie_1.get("cast"))
# 如果key不存在的話，程式會回傳None，不會出現錯誤訊息
print(movie_1.get("cast", "not found"))
# 可以自己設定空訊息
print('**********************************')
# 如果一次要update很多value at a time 用update method就會比較方便
print(movie_1)
temp_dict = {'writer': 'Robert Rodat',  # 編劇
             'stars': ['Tom Hanks', 'Matt Damon', 'Tom Sizemore'],  # 明星
             'Oscar ': ['Best Director', 'Best Cinematography', 'Best Sound', 'Best Film Editing',
                        'Best Effects, Sound Effects Editing'],
             'star': ['osper1', 'osper2']
             }

movie_1.update(temp_dict)
print('1. ', movie_1)
del movie_1['star']
print('2. ', movie_1)
writer = movie_1.pop('writer')
print('3. ', movie_1)
print('**del 语句和 pop() 函数作用相同，pop() 函数有返回值。********************************')
d1 = {'1': 'osper',
      '2': 'osepr2',
      '3': "osper3"}
print(d1)
print('len', len(d1))
for i in d1:
    print(i, '測試測試' + d1.get(i))
aa = d1.keys()
print('keys', aa)
for i in aa:
    print(i)
bb = d1.values()
print('values', bb)
print('**********************"//*[@id=\'rcnt\']"*************************')
# item method
i = d1.items()
print(i)
print('******************************************')
movie_1 = {'name': 'Saving Private Ryan',
           'year': 1998,
           'director': 'Steven Spielberg'}
movie_2 = dict(name='Saving Private Ryan',
               year=1998,
               director='Steven Spielberg')
movie_3 = {'name': 'Catch Me If You Can',
           'year': 2002,
           'director': 'Steven Spielberg'}
movie_4 = {'year': 1998,
           'name': 'Saving Private Ryan',
           'director': 'Steven Spielberg'}
print(movie_1 == movie_2)
print(movie_1 is movie_2)
for k, v in movie_1.items():
    print(k, v)
for key in movie_1:
    print(key, movie_1[key])
print('**********************************')
dict_squares = {}
for i in range(6):
    dict_squares[i] = i**2
print(dict_squares)
my_squares = {i: i ** 2 for i in range(6)}
print(my_squares)
print(type(my_squares))
# for i in my_squares:
#     print('Key is', i, 'Value is', my_squares[i])
