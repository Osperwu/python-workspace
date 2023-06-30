"""
loop
"""
# theBeatles = ['John Lennon', 'Paul McCartney', 'Ringo Starr', 'George Harrison']
# for i in range(len(theBeatles)):
#     print(theBeatles[i])

# for i in range(10):
#     print(i, end=" ")
    
# print() #換行
# for i in range(20, 4, -2):
#     print(i, end=" ")

a = '練習題九九乘法表'
print(a)

for i in range(1,10):
    for j in range(1,10):
        if j != 9:
            print("\t", i*j ,end=" ")
        else:
            print("\t", i*j)
    # if i == 1:
    #   break
print('******************')

sequences = [0, 1, 2, 3, 4, 5]
i = 0
while 1==1: #判斷條件值為1, 代表迴圈永遠成立
    print(sequences[i], end = " ")
    i = i + 1
    if i == len(sequences):
        print("No elements left.")
        break
