from math import gcd

def dao_nguoc(n):
    return int(str(n)[::-1])   # đảo chuỗi rồi chuyển lại số

def la_than_thien(n):
    d = dao_nguoc(n)
    return gcd(n, d) == 1

a, b = input("Nhập a, b: ").split()
a, b = int(a), int(b)

dem = 0
for n in range(a, b + 1):
    if la_than_thien(n):
        print(n)
        dem += 1

print(dem)