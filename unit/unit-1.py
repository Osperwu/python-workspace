#1.print method
print("hello world")
print('///////////////////////')
#2.Variable and type
a = 123
print(type(a))
b='456'
print(type(b))
c=1.213
print(type(c)) 
d=True
print(type(d)) 
print('///////////////////////')
'''運算子'''
e = 9
f = 3
print(e+f)
print(e-f)
print(e*f)
print(e / f)
print(e // f)
print(e**f)
print('///////////////////////')
"""轉型"""
g = 123
h = '456'
print(g + int(h))
print(str(g) + h)
"""input"""
#i = int(input('hello =>'))
#print(i)
#j = str(input('hello =>'))
#print(j)
#name = input('Hello, what is your name?  ')
#print('Hi, ', name)
"""if else"""
battery = 10
if battery > 70:
    print('no charge')
elif battery < 30:
    print('need charge')
elif battery == 10:
    print('charge')
else:
    print("power middle")

h = 180
w = 85
grade = 80

# 身高超過175或是體重超過80，看起來就很大隻
if h > 175 or w > 80:
    print('big dude')

# 成績高於70但是不高於90，就是個普通學生
if grade > 70 and grade < 90:
    print('noraml')
"""loop"""
for i in range (6):
    print(i)
