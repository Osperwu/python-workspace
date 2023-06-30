users = dict([('user1', 'Daniel'), ('user2', 'Sam')])
for i, user in users.items():
    print(i, user)
student = dict([('student1', 'James'), ('student2', 'Ray')])
temp_users = users.copy()
temp_users.update(student)
print(temp_users)
print(dict(users.items() | student.items()))
print({**users, **student})
print('***********************')
user_info = dict(ADaniel=200, BSam=30, CJack=4)
# for u in sorted(user_info.values()):
#     print(u, user_info[u])

# 根據值進行排序，得到排序後的鍵列表
sorted_keys = sorted(user_info, key=user_info.get)

# 取得最大值對應的鍵
max_key = max(user_info, key=user_info.get)

# 輸出排序後的鍵列表和最大值對應的鍵
print("Sorted keys:")
for key in sorted_keys:
    print(key)

print("Key with max value:", max_key)
