# 摩托車類別
class Motorcycle:
    # 建構式
    def __init__(self, size):
        self.size = size
        # 方法(Method)

    def ride(self):
        # print()
        return f"Ride {self.size}KG motorcycle"


honda = Motorcycle(6)
print(honda.ride())
