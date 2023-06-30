"""
sample.txt =
abc
def
ghi
"""

f = open('sample.txt')
print('1.' + f.read(1))
print('2.', f.tell())
print('3.' + f.readline())
print('4.', f.tell())
f.close()
