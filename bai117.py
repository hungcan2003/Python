n = input("Nhap n ")  # đọc dạng chuỗi để dễ cắt

S = 0
length = len(n)

for start in range(length):          # vị trí bắt đầu
    for end in range(start + 1, length + 1):   # vị trí kết thúc
        sub = int(n[start:end])      # cắt chuỗi con → chuyển số
        S += sub * sub               # cộng bình phương

print(S)