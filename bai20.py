a = int(input("Nhap so tien hang (a):"))
b = int(input("Nhap so tien khach tra (b):"))

if a > b:
    print(f"khach hang con thieu :{a-b}")
elif a == b:
    print(f"Cam on khach hang. Hen gap lai")
else:
    X = b - a 
    print(f"so tien {X} duoc thoi lai thanh")
    menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    tong_so_to = 0
    tong_so_loai = 0

    for mg in menh_gia:
        so_to = X // mg
        X = X % mg
        if so_to > 0:
            print(f"Loai {mg} gom {so_to} to")
            tong_so_loai += 1 
        tong_so_to += so_to

    print(f"TONG CONG CO {tong_so_to} TO")
    print(f"tong so loai = {tong_so_loai}")
    input("\nNhan Enter de ket thuc...")
    print("Cam on khach hang. Hen gap lai")