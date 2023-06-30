from typing import Dict

sum = [0, 6, 0]
# for i in range(int(input())):
#     sum[int(input())%3] += 1

print(' '.join([str(i) for i in sum]))

print(' '.join(str(s) for s in [1, 3, 5, 7, 9]))

print(' '.join(str(s) for s in (2, 4, 6, 8, 10)))


# cipher = input()
# plain = ''
# for s in cipher:
#     plain += chr(ord(s) - 7)
# print(plain)


def add_end(L, y=10, x=0):
    if L is None:
        L = []
    L.append('END' + str(y) + str(x))
    return L


ll = add_end([1, 3, 5], 0, 3)
print(ll)


def foo(x, *args):
    for i in args:
        if not isinstance(i, int):
            print(i, i != int, type(i))
            raise Exception('錯誤型別')
        else:
            x = i + x

    print('ANS = ', x)


foo(1, 2, 3, 4)


def create_cycle():
    # create a list x
    x = [1.2, 1]

    #  這裡創建了一個引用循環，因為 x 包含對自身的引用。
    x.append(x)
    print(x)


create_cycle()

data_source1 = ['Bob', 'Alice', 'John', 'Cindy']
for i, name in enumerate(data_source1):
    print(name)


def foo1(x, *args, **kw):
    print(x)
    print(args)
    print(kw)


foo1(1, 2, 3, 4, y=1, a=2, b=3, c=4)

print('*************************************')


def foo2(a, b, c, d):
    print(a)
    print(b)
    print(c)
    print(d)


diccccc = {"a": 2, "b": 3, "c": 4, "d": 5}
foo2(**diccccc)
foo2(*(1, 2, 3, 4))


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
person('osper', 27, **extra)


def person2(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)


person2('Jack', 25, city='Beijing', addr='Chaoyang', zipcode=123456)


def person3(name, age, *, city, job, add):
    print(name, age, city, job)


person3('Jack', 260, city='Beijing', job='Engineer', add=1)

osp = {'name': 'osper', 'age': 30, 'city': 'Taipei', 'job': 'driver', 'add': '台北市'}
person3(**osp)

person3('Jack11', 99, city=None, job='Engineer', add=1)

print('********************')


def person4(name, age, city, job):
    print(name, age, city, job)


def person5(name, age, *, city, job):
    print(name, age, city, job)


person4('Jack', 1, '台北', '工程師''台北''666')
# person5('Jack', 2, 'Beijing', 'Engineer')
person4('Jack', 3, city=None, job='Engineer')
person5('Jack', 4, city='Beijing', job='Engineer')

person('osper', 5, city=6, job='Engineer')
