def Nhapn():
    print ("Nhập một số nguyên dương: ")
    n = int(input())
    while n <= 2 or n >= 10:
        print("Vui lòng nhập một số nguyên dương từ 2 đến 10: ")
        n = int(input())
    return n

def XetSoStrobogrammatic(n): 
    digits = set()
    map = {0, 1, 6, 8, 9}
    for digit in str(n):
        digit = int(digit)
        if digit not in map:
            return False
    return True

def xettu1denn(n):
    for i in range(1, n + 1):
        if XetSoStrobogrammatic(i):
            print(i, end=' ')
    print()  # In xuống dòng sau mỗi số strobogrammatic
n = Nhapn()
xettu1denn(n)


def Nhapn():
    print ("Nhập một số nguyên dương: ")
    n = int(input())
    while n <= 2 or n >= 10:
        print("Vui lòng nhập một số nguyên dương từ 2 đến 10: ")
        n = int(input())
    return n

def XetSoStrobogrammaticC(n): 
    digits = set()
    map = {0, 1, 2, 5, 6, 8, 9}
    for digit in str(n):
        digit = int(digit)
        if digit not in map:
            return False
    return True

def xettu1denn1(n):
    for i in range(1, n + 1):
        if XetSoStrobogrammaticC(i):
            print(i, end=' ')
    print()  # In xuống dòng sau mỗi số strobogrammatic
xettu1denn1(n)