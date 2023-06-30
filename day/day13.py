import random

nums = [(1, 2, 3), (4, 5, 6), (7, 8, 0)]
for i, (a, b, c) in enumerate(nums):
    print(i, a, b, not c)
print('****************')
# 如果 c 是非零數字，那麼 not c 的結果將是 False。如果 c 是零，則 not c 的結果將是 True。

for i, v in enumerate(nums):
    print(i, v)
print('****************')

# d = {
#     1: 'a',
#     2: 'b',
#     3: 'c'
# }
#
# for i, v in enumerate(d.items(), start=d.__len__()):
#     print(i, v)
listA = ['f', 'a', 'r', 'A', 'z', 'T', 'o']
listA.sort()
listA.reverse()
print('1.', listA)
listA = ['f', 'a', 'r', 'A', 'z', 'T', 'o']
listA.sort()
second = list(reversed(listA))
print('2.', second)
listA = ['f', 'a', 'r', 'A', 'z', 'T', 'o']
c = sorted(listA, reverse=True)
print('3.', c)
print('*************slicing*******************')
names = ('Daniel', 'O我sper', 'Tom')
var2 = names[1][-5]
print(var2)
print('*************format *******************')
nums = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for i, j, k in nums:
    print('{0},{1},{2}'.format(i, j, k))
print('2.************************')
for i, v in enumerate(nums):
    print(i, v)
print('3.************************')
for i in nums:
    print(i)
for i in range(6):
    print('i', i, '+ r', random.randint(1, 10), end='\n')
print('Daniel'[::-1])
print('*************"*,**"*******************')


def count_sum(num1, *nums):
    sum = num1
    for n in nums:
        sum += n
    return print(sum)


count_sum(5)
count_sum(5, 1, 2)


def count_sum(n1, n2, n3):
    return print(n1 + n2 + n3)


numssss = [1, 2, 3]
count_sum(*numssss)
print('*************"dictionaries"*******************')


def count_sum_d(item1, item2, item3):
    return item1 + item2 + item3


item_list = {'item1': 20, 'item2': 30, 'item3': 40}
d1 = count_sum_d(*item_list)
print(d1)
# 90


# def count_sumd(**nums):
#     sum = 0
#     for num in nums.values():
#         sum += num
#     return sum
#
#
# sumd = count_sumd(item1=20, item2=30, item3=40)
# print('sum dictionary', sumd)

users = {'user1': 'Daniel', 'user2': 'Sam'}
student = {1: 'James', 'student2': 'Ray'}
ans = {**users, **student}
print(ans)
