# 3.3:Python數據類型（列表:List）
# 在Python中，複合數據類型分別有三種：Tuple（元組）、Set（集合）與List（列表）。
# 然後今天教的複合數據類型就是這三類之中最easist的一類：List（列表）

a = ['a','b','c',3] #创建两个列表
b = [4,7,'love','to','osper',',','never','change']
print(a,b)
print(a[0:1:3]) #输出指定列表被切割后的指定数据
print(b[1:7])
print(a[3]) #输出指定索引搜索的数据
print(b[7])
a[0:3]='A','B','C'  #修改列表中指定数据，即可以直接修改
print(a)
b.append(347)   #append()函数用于在制定列表末尾添加新数值
print(b)
a[1]=[] #移除a列表中指定索引数据
print(a)
print('a列表数据个数:',len(a),'b列表数据个数:',len(b))  #len()函数用于统计列表数据个数
c=[0,1]   #生成一个嵌入式列表
d=[2,3]
e=[c,d]
print(e)
