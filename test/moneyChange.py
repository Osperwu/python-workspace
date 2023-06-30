"""
請輸入所需要的金額: 3866
2000 需要    1張 , 共      2000元
1000 需要    1張 , 共      1000元
500  需要    1張 , 共       500元
200  需要    1張 , 共       200元
100  需要    1張 , 共       100元
50   需要    1個 , 共        50元
10   需要    1個 , 共        10元
5    需要    1個 , 共         5元
1    需要    1個 , 共         1元
"""
# // 兩個'/'可以無條件捨去
# 除完又乘是為了有效運用變數
twd =int( input('請輸入整數金額'))
x2000 = twd // 2000 * 2000
x1000 = (twd - x2000) // 1000 * 1000
x0500 = (twd - x2000 - x1000) // 500 * 500
x0200 = (twd - x2000 - x1000 - x0500) // 200 * 200
x0100 = (twd - x2000 - x1000 - x0500 - x0200) // 100 * 100
x0050 = (twd - x2000 - x1000 - x0500 - x0200 - x0100) // 50 * 50
x0010 = (twd - x2000 - x1000 - x0500 - x0200 - x0100 - x0050) // 10 * 10
x0005 = (twd - x2000 - x1000 - x0500 - x0200 - x0100 - x0050 - x0010) // 5 * 5
x0001 = (twd - x2000 - x1000 - x0500 - x0200 - x0100 - x0050 - x0010 - x0005) // 1 * 1


# {:<4d} 靠左對齊 4格
print("{:<4d} 需要 {:4.0f}張 , 共{:10d}元".format(2000, x2000 // 2000, x2000))
print("{:<4d} 需要 {:4.0f}張 , 共{:10d}元".format(1000, x1000 // 1000, x1000))
print("{:<4d} 需要 {:4.0f}張 , 共{:10d}元".format(500, x0500 // 500, x0500))
print("{:<4d} 需要 {:4.0f}張 , 共{:10d}元".format(200, x0200 // 200, x0200))
print("{:<4d} 需要 {:4.0f}張 , 共{:10d}元".format(100, x0100 // 100, x0100))
print("{:<4d} 需要 {:4.0f}個 , 共{:10d}元".format(50, x0050 // 50, x0050))
print("{:<4d} 需要 {:4.0f}個 , 共{:10d}元".format(10, x0010 // 10, x0010))
print("{:<4d} 需要 {:4.0f}個 , 共{:10d}元".format(5, x0005 // 5, x0005))
print("{:<4d} 需要 {:4.0f}個 , 共{:10d}元".format(1, x0001 // 1, x0001))
