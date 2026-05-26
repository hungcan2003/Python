# Bài 9: Hình khối chữ nhật
chieu_dai = float(input("Nhập chiều dài đáy hình khối chữ nhật (cm):> "))
chieu_rong = float(input("Nhập chiều rộng đáy hình khối chữ nhật (cm):> "))
chieu_cao = float(input("Nhập chiều cao hình khối chữ nhật (cm):> "))
so_le = int(input("Số lượng số lẻ cần hiển thị:> "))
dien_tich = chieu_dai * chieu_rong
the_tich = chieu_dai * chieu_rong * chieu_cao
# Cách 1: 
print(f"Cách 1: Diện tích đáy hình chữ nhật = {dien_tich:.{so_le}f}cm\u00b2")
print(f"Cách 1: Thể tích hình khối = {the_tich:.{so_le}f}cm\u00b3")
# Cách 2:
print(f"Cách 2: Diện tích đáy hình chữ nhật = {dien_tich:.{so_le}f}cm²")
print(f"Cách 2: Thể tích hình khối = {the_tich:.{so_le}f}cm³")
def bang_cuu_chuong(a, b):
    if a < b:
        for i in range(a, b + 1):
            print(f"--- Bảng {i} ---")
            for j in range(1, 11):
                print(f"{i} x {j} = {i*j}")
    else:
        for i in range(a, b - 1, -1):
            print(f"--- Bảng {i} ---")
            for j in range(1, 11):
                print(f"{i} x {j} = {i*j}")

a, b = map(int, input("Nhập a, b: ").split(','))
bang_cuu_chuong(a, b)
#bài 2 kiểm tra nguyên tố:
def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            return False
    return True
n = int(input("Nhập n: "))
if la_nguyen_to(n):
    print(f"{n} là số nguyên tố")
else:
    print(f"{n} không phải số nguyên tố")
#bài 3 kiểm tra số nguyên dương <n:
def liet_ke_nguyen_to(n):
    return [i for i in range(2, n) if la_nguyen_to(i)]

n = int(input("Nhập n: "))
print(liet_ke_nguyen_to(n))
#bài 4 đếm số nguyên tố <n:
def dem_nguyen_to(n):
    return len(liet_ke_nguyen_to(n))   

n = int(input("Nhập n: "))
print(f"Có {dem_nguyen_to(n)} số nguyên tố nhỏ hơn {n}")
#bài 5 ước số của n là số nguyên tố:
def uoc_nguyen_to(n):
    uoc_so = [i for i in range(1, n + 1) if n % i == 0]
    print(f"Các ước số của {n}: {uoc_so}")
    ket_qua = [i for i in uoc_so if la_nguyen_to(i)]
    print(f"Ước vừa là số nguyên tố: {ket_qua}")

n = int(input("Nhập n: "))
uoc_nguyen_to(n)
