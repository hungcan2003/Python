
def TachSo(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    return digits


def GopSo(digits):
    n = 0
    for digit in digits:
        if digit == 6:
            digit = 9
        elif digit == 9:
            digit = 6
        n = n * 10 + digit
    return n


def XetSoStrobogrammatic(n):
    map = {0, 1, 6, 8, 9}
    digits = TachSo(n)
    for digit in digits:
        if digit not in map:
            return False
    if n == GopSo(digits):
        return True
    return False



def XetSoStrobogrammaticC(n):
    map = {0, 1, 2, 5, 6, 8, 9}
    digits = TachSo(n)
    for digit in digits:
        if digit not in map:
            return False
    if n == GopSo(digits):
        return True
    return False


def XetSoNguyenTo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True



def xettu1denn():
    print("Cau A:")
    for i in range(1000000):
        if XetSoStrobogrammatic(i):
            print(i, end=' ')
    print()
    print()




def insoStrobogrammaticNguyenTo(n):
    print("Cau B:")
    for i in range(2, n + 1):
        if XetSoNguyenTo(i) and XetSoStrobogrammatic(i):
            print(i, end=' ')
    print()
    print()



def xuat2():
    print("Cau C:")
    for i in range(1000000):
        if XetSoStrobogrammaticC(i):
            print(i, end=' ')
    print()
    print()


def insoStrobogrammaticNguyenTo1(n):
    print("Cau D:")
    for i in range(2, n + 1):
        if XetSoNguyenTo(i) and XetSoStrobogrammaticC(i):
            print(i, end=' ')
    print()
    print()



def XetCacSoKhongPhaiStrobogrammaticvaSoNguyenTo(n):
    print("Cau E:")
    for i in range(2, n + 1):
        if not XetSoStrobogrammatic(i) and not XetSoNguyenTo(i):
            print(i, end=' ')
    print()
    print()

# Dao nguoc so
def DaonguocSo(n):
    reversed_n = 0
    while n > 0:
        digit = n % 10
        reversed_n = reversed_n * 10 + digit
        n //= 10
    return reversed_n



def InraSoDaoNguocNguyenTo(n):
    print("So nguyen to dao nguoc:")
    for i in range(2, n + 1):
        dao = DaonguocSo(i)
        if XetSoNguyenTo(i) and XetSoNguyenTo(dao) and dao != i:
            print(i, end=' ')
    print()



def main():
    xettu1denn()
    insoStrobogrammaticNguyenTo(1000000)
    xuat2()
    insoStrobogrammaticNguyenTo1(1000000)
    XetCacSoKhongPhaiStrobogrammaticvaSoNguyenTo(1000000)
    InraSoDaoNguocNguyenTo(1000000)

main()