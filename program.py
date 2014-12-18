import os

def somefunc(yay):
    return yay + " another part"

print(somefunc("this and"))
def sayhi(num):
    result = ""
    for i in range(num):
        result += "["+str(i)+"] Hello world!\r\n"
    return result
print(sayhi(3))
