# l = ['52412 D02 RD1-Bruce 十三香滷牛腱 140', '52428 D02 RD1-黃騰瑩 韓式泡菜牛 130']
#
# total = 0
# for item in l:
#     # 提取最後的數字
#     last_num = int(item.split(" ")[-1])
#     print(last_num)
#     # 將最後的數字相加
#     total += last_num
#
# print(total)

from datetime import datetime
currentDateAndTime = datetime.now()
print(str(currentDateAndTime).split(".")[0])
currentTime = currentDateAndTime.strftime("%y -%m -%d %H:%M:%S")
print("The current time is", currentTime)