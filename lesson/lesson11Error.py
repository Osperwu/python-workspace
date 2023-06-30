try:
    a = int(input())
    b = int(input())
    c = a/b
except ZeroDivisionError:
    print("Cannot divide by 0!")
except:
    print("Wrong input")
else:
    print("The answer is " + str(c))
finally:
    print("Program finished")