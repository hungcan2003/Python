#Bài ÔN TẬP LAMBDA
# 1. Trị tuyệt đối
f1 = lambda n: abs(n)
# 2. Giá trị n + 15
f2 = lambda n: n + 15
# 3. Tích x * y
f3 = lambda x, y: x * y
# 4. n có là bội số của 13 hoặc 19?
f4 = lambda n: n % 13 == 0 or n % 19 == 0
# 5. Diện tích hình tròn
import math
f5 = lambda r: math.pi * r ** 2
# 6. Chu vi hình chữ nhật
f6 = lambda d, r: 2 * (d + r)
# 7. Số chính phương (căn bậc 2 là số nguyên)
f7 = lambda n: int(n**0.5) ** 2 == n
# 8. Số nguyên tố (gọi lại hàm đã có)
def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
f8 = lambda n: la_nguyen_to(n)
# 9. Kiểm tra 3 cạnh có tạo thành tam giác không
def kiem_tra_tam_giac(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Tam giác đều"
        elif a == b or b == c or a == c:
            return "Tam giác cân"
        elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return "Tam giác vuông"
        else:
            return "Tam giác thường"
    else:
        return "Không tạo thành tam giác"
# Dùng lambda để gọi.
f9 = lambda a, b, c: kiem_tra_tam_giac(a, b, c)
# Test 
print(f9(3, 4, 5))   
print(f9(5, 5, 5))   
print(f9(1, 2, 10))  