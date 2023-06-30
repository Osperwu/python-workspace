'''
'r' Read text file (default)
'w' Write text file (如果存在的話會 overwrites)
'x' Write text file (如果檔案已經存在則會丟出 FileExistsError)
'a' Append to text file (會從檔案的結尾開始新增內容)
'rb' Read binary file
'wb' Write binary file (如果存在的話會 overwrites)
'w+b' Open binary file (可讀取跟寫入)
'xb' Write binary file (如果檔案已經存在則會丟出 FileExistsError)
'ab' Append to binary file (會從檔案的結尾開始新增內容)
'''
with open('sample.txt', 'r') as f:
    l = f.readlines()
    print(type(l))
    print(len(l))
    print(f.closed)


for line in l:
    print(line.strip())

print(f.closed)
