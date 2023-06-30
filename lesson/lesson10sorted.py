movieList = ["The Shape of Water", "Moonlight", "Superman", "Birdman", "Argo", "Spotlight"]
a = sorted(movieList)
b = sorted(movieList, reverse=True)
print('正常排序', a)
print('反轉排序', b)
print('*******************************')
dic = {"2017": "The Shape of Water",
       "2016": "Moonlight",
       "2014": "Birdman",
       "2015": "Spotlight"}
print('排序過的字典', sorted(dic))
for year in sorted(dic):
    print(year + ":" + dic[year])
print('*******************************')
movieList = ["The Shape of Water", "Moonlight", "Superman", "Birdman", "Argo", "Spotlight", "aaaaa"]
movieList = sorted(movieList, key=len)
print('字串長度:', movieList)
print('*******************************')
dic = {2017: "The Shape of Water",
       2016: "Moonlight",
       2014: "Birdman",
       2015: "Spotlight"}

l = sorted(dic.items(), key=lambda d: d[1])
print(type(l))


def dic_value(d):
    return d[0]


print(sorted(dic.items(), key=dic_value))
print('*******************************')
mylist = ["pen", "pineapple2", "pineapple1", "applepens", "apple"]
print(sorted(mylist, key=len))


def multi_sort(s):
    return len(s), s


print(sorted(mylist, key=multi_sort))
