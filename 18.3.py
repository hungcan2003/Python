import math


LIMIT = 1000000

is_palindrome = lambda n: str(n) == str(n)[::-1]

print("CÁC SỐ PALINDROME TỪ 1 ĐẾN 1 TRIỆU (In thử 30 số đầu tiên)")
palindrome_numbers = [x for x in range(1, LIMIT + 1) if is_palindrome(x)]
print(palindrome_numbers[:30], "... \n")



is_prime_palindrome = lambda n: str(n) == str(n)[::-1] and n > 1 and all(n % i != 0 for i in range(2, int(math.isqrt(n)) + 1))

print(" CÁC SỐ NGUYÊN TỐ PALINDROME DƯỚI 20.000 ")

prime_palindrome_under_20k = [x for x in range(1, 20000) if is_prime_palindrome(x)]
print(prime_palindrome_under_20k, "\n")

print("CÁC SỐ NGUYÊN TỐ PALINDROME TỪ 1 ĐẾN 1 TRIỆU")
prime_palindrome_numbers = [x for x in range(1, LIMIT + 1) if is_prime_palindrome(x)]
print(prime_palindrome_numbers[:30], "...")