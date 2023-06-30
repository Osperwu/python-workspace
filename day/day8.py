nums = range(10)
list1 = list(nums)
list2 = list(range(1, 20, 2))
# print(list1)
# print(list2)
#產生一個新的list
print(list1 + list2)
print(type(list1 + list2))
#原list1增加list2
# print(list1.append(list2))
# print(list1)
#原list1增加list2裡面的值
print(list1.extend(list2))
print(list1)

items = [1,'a','5',2.5,[0],'夫','不','鋪','書']
items.sort(key=str)
print(items)
import locale

# 設置區域設置為中文（中國）
locale.setlocale(locale.LC_COLLATE, 'zh_CN.UTF-8')

my_list = ['我', '是', '一', '個', '列表']

# 使用 sort() 方法進行排序，並指定 key 參數
my_list.sort(key=locale.strxfrm)

print(my_list)  # ['個', '列表', '我', '是', '一']
