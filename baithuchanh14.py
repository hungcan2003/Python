X = int(input("Nhap so tien can doi(X) "))
menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]
tong_so_to = 0

for mg in menh_gia:
    so_to = X // mg
    X = X % mg
    tong_so_to += so_to
    print(f"Loai {mg} gom {so_to} to")

print(f"TONG CONG CO {tong_so_to} TO")
