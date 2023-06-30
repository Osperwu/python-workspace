# 3.4:Python數據類型（Tuple:元組）
# 在Python中，元組的語法與列表差不多，不同之處就是元組使用小括號（），
# 且括號中元素不能被改變，創建元組可以不需要括號;而列表是使用中括號[]。
# 因此想要把列表轉換為元組或元組轉換為列表，只需要改一下括號即可

a = ('C/c++','Python',2)	#创建两个元组
b = ["Python菜中菜的菜鸟1","Love to lxx for Li wenli","never change"]
print(type(a))
print(type(b))
print(a,b)

a = ('C/C++','Python',2)	#创建两个元组
b = "Python菜中菜的菜鸟2","Love to lxx for Li wenli","never change"
c = a+b #相互结合
print(c)

a = ('C/C++','Python',2)	#创建两个元组
b = "Python菜中菜的菜鸟","Love to lxx for Li wenli","never change"
c = a+b #相互结合
print(c)
del c
# print(c)

a = ('C/C++','Python',2)	#创建两个元组
b = "Python菜中菜的菜鸟","Love to lxx for Li wenli","never change"
c = a+b #相互结合
print(len(c))#输出c元组内数据个数
print(c*2)#复制输出
print(b in ("Python菜中菜的菜鸟","Love to lxx for Li wenli","never change"))
#判断元素是否存在
for c in ("Python菜中菜的菜鸟","Love to lxx for Li wenli","never change",'C/C++','Python',2):
      print(c,) #迭代输出

a = ['C/C++','Python',2,4]	#创建列表
b = ["Python菜中菜的菜鸟","Love to lwl for Li wenli","never change"]
c = a+b #相互结合
c = tuple(c)#强制转换为元组
print(len(c))#输出列表内数据个数
d = ('3','4','8')
print(max(d))#输出d元组内最大数值
print(min(d))#输出d元组内最小数值，max()是判断最大值函数，min()反之

