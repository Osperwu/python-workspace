'''range'''
# nums = range(10)
# list1 = list(nums)
# list2 = list(range(1, 20, 2))
# print(list1)
# print(list2)
# print(type(list1 + list2))
# print(list1.append(list2))
# print(list1)
# print(list1.extend(list2))
# print(list1)
'''tuples'''
names = 'osper', 'osp1'
names2 = 'osper', 'osp2'
names3 = names + names2
print(names + names2)
print('osper' not in names3)
a = 0
for name in names3:
    if (name == 'osper'):
        # a += 1
        a = a+1
        # print(a)
print(a)
