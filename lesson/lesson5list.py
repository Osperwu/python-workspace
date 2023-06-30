# thriller = ['Thriller', 'Billie Jean', 'Beat It']
# # print(thriller)
# # print(len(thriller))
# # print(thriller[0])
# # print(thriller[-1],thriller[len(thriller)-1])
# # print(thriller[0:3])
# # print(thriller[2:])
'''append'''
# thriller = ['Thriller', 'Billie Jean', 'Beat It']
# thriller.append('That Girl is Mine')
# print('append',thriller)
'''inseret'''
# thriller = ['Thriller', 'Billie Jean', 'Beat It']
# thriller.insert(1, 'That Girl is Mine')
# print(thriller)
# thriller.insert(-1, 'That Girl is Mine')
# print(thriller)
'''extend'''
# bad_1 = ['Bad', 'Smooth Criminal', 'Speed Demon']
# bad_2 = ['Man in the Mirror', 'Dirty Diana']
# bad_1.extend(bad_2)
# print(bad_1)
# #insert 會直接將串列直接放入指定位置
# bad_1 = ['Bad', 'Smooth Criminal', 'Speed Demon']
# bad_2 = ['Man in the Mirror', 'Dirty Diana']
# bad_1.insert(1, bad_2)
# print(bad_1)
'''remove'''
# bad = ['Bad','Smooth Criminal','Speed Demon','Man in the Mirror','Dirty Diana']
# bad.remove('Smooth Criminal')
# print(bad)
'''pop'''
bad = ['Bad','Smooth Criminal','Speed Demon','Man in the Mirror','Dirty Diana']
# popped = bad.pop(1)
bad.pop(len(bad) - 1)
print(bad)
# print(popped)
