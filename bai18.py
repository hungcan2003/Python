LIMIT = 1000000


is_abundant = lambda n: sum(i for i in range(1, n // 2 + 1) if n % i == 0) > n

print("CÁC SỐ PHONG PHÚ TỪ 1 ĐẾN 1 TRIỆU (In thử 20 số đầu tiên) ")
abundant_numbers = [x for x in range(1, LIMIT + 1) if is_abundant(x)]
print(abundant_numbers[:20], "... \n")



is_increasing = lambda n: all(str(n)[i] <= str(n)[i+1] for i in range(len(str(n)) - 1))

print("--- CÁC SỐ TĂNG DẦN TỪ 1 ĐẾN 1 TRIỆU (In thử 20 số đầu tiên) ---")
increasing_numbers = [x for x in range(1, LIMIT + 1) if is_increasing(x)]
print(increasing_numbers[:20], "... \n")


is_armstrong = lambda n: sum(int(digit) ** len(str(n)) for digit in str(n)) == n

print("--- CÁC SỐ ARMSTRONG TỪ 1 ĐẾN 1 TRIỆU ---")
armstrong_numbers = [x for x in range(1, LIMIT + 1) if is_armstrong(x)]
print(armstrong_numbers)