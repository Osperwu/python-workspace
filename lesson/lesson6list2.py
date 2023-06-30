'''sort'''
# bad = ['Bad', 'Smooth Criminal', 'Speed Demon',
#        'Man in the Mirror', 'Dirty Diana', '我','是']
# print(bad)
# bad.sort()
# print(bad)
# r = bad.sort(reverse=True)
# print(r)

# num = [23, 4, 53, 5 ,35, 6]
# num.sort()
# print(num)
'''reverse'''
# num.sort(reverse=True)
# print(num)
'''max、min、sum'''
# num = [23, 4, 53, 5 ,35, 6]
# print(max(num))
# print(min(num))
# print(sum(num))
# bad = ['Bad', 'Smooth Criminal', 'Speed Demon',
#        'Man in the Mirror', 'Dirty Diana',]
# print(max(bad))
# print(min(bad))
# print(len(bad))
# print(sum(bad))#)會報錯
'''index'''
# bad = ['Bad','Smooth Criminal','Speed Demon','Man in the Mirror','Dirty Diana','模','蒲','福']
# print('回索引值',bad.index("Dirty Diana"))
'''reverse'''
# bad = ['Bad','Smooth Criminal','Speed Demon','Man in the Mirror','Dirty Diana','模','蒲','福']
# print(bad)
# print()
# bad.reverse()
# print(bad)
# bad3 = bad.sort(reverse=True)
# print(bad)
# print(bad3)

# '''sorted'''
# bad = ['a','b','c']
# bad2 = sorted(bad,reverse=True)
# bad2.append('ccc')
# bad2.append('ddd')
# bad2.sort(reverse=True)
# print(bad)
# print(bad2)

'''in'''
# bad = ['Bad','Smooth Criminal','Speed Demon','Man in the Mirror','Dirty Diana']
# bad = ['Bad','Smooth Criminal','Speed Demon','Man in the Mirror','Dirty Diana']
# print("Heal the World" in bad)
# print("Smooth Criminal" in bad)

'''enumerate function'''
# dangerous = ['Jam', 'In the Closet', 'Remember the Time',"Heal the World","Black or White","Who Is It","Give In to Me", "Dangerous"]
# for index, song in enumerate(dangerous):
#     print(index, song)

# dangerous = ['Jam', 'In the Closet', 'Remember the Time',"Heal the World","Black or White","Who Is It","Give In to Me", "Dangerous"]
# for i,song in enumerate(dangerous,start=2):
#     print(i*2,song)

'''str join'''
# dangerous = ['Jam', 'In the Closet', 'Remember the Time',"Heal the World","Black or White","Who Is It","Give In to Me", "Dangerous"]
# dangerous_str = '**'.join(dangerous)
# print(dangerous_str)

# dangerous = ['Jam', 'In the Closet', 'Remember the Time',"Heal the World","Black or White","Who Is It","Give In to Me", "Dangerous"]
# dangerous_str = '/ '.join(dangerous)
# new_dangerous_list = dangerous_str.split("/ ")
# print(new_dangerous_list)

'''str split'''
# lst = [int(num) for num in input().split()]
# print(lst)

'''切割 轉型 迴圈 應用'''
osp = '1,2,3'

a = osp.split(',')
c = []
for n in a:
    b = int(n)
    c.append(b)
print(c)

lst = [int(num) for num in osp.split(',')]
print(lst)