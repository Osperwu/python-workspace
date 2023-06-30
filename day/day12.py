# def print_hell(a):
#     print('hello', a)
# print(id(print_hell(2)))
# print(print_hell(1).__doc__)
# help(print_hell(1))
print('*******************')
global_num = 1


def print_numbers():
    local_num = 5
    print('global num : {}'.format(global_num))
    print('local num : {}'.format(local_num))
    print('built-in variables : {}'.format(dir))


print_numbers()

print('*******************')


def say_hello(name='Python'):
    print('Hello {}'.format(name))


say_hello()


def add_nums(num1, num2=10):
    return num1 + num2


a = add_nums(2)
print(a)
print('******************')


def to_Set(value, default_set=None):
    if default_set is None:
        default_set = set([])
        default_set.add(value)
        return default_set
    else:
        default_set.append(value)
        return default_set


s1 = to_Set(5)
print('s1', type(s1))
print('s1', s1)
s2 = to_Set('Daniel')
print('s2', type(s2))
print('s2', s2)
nums = [1, 2, 3, 4, 2, 5]
s = to_Set(5, nums)
print('s3', type(s))
print('s3', s)
