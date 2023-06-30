a = 'Hello','LWL'
b = 'Hello''LWL'	
#注意字串符a与b的区别，如果有逗号，
#那么输出时将会是两个字串符一起输出，如
#果没有输出将会两个字串符相互结合输出

c,d= 'Hiha','OSP'
print(a)
print('b=',b)
print(c,d)
print(c+d)
print('*************')
print('1. = ',b[0:-2])
print('2.',c)
print('3. ' + c[0:2])
print('4. '+ d[0:-1])

print('*************')
print(c*2,d*2)#各输出两次
print((c+d)*2)#结合输出两次
print('Hello,\nLWL')
print(r',,,,Hello,LWL')#加了r后转义字符失效
e='Love osper 1314'
print(e[0],e[5])#输出指定索引位置的字母
print(e[0],e[-2],e[3])#Python与C语言字串符不同的地方在于Python字串符是不可以被改变的，
                      #如果向一个指定索引赋值，那么将会错误

