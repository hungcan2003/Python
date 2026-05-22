import math


LIMIT = 100


is_prime_c1 = lambda n: n > 0 and sum(1 for i in range(1, n + 1) if n % i == 0) == 2

print(" SỐ NGUYÊN TỐ TỪ 1 ĐẾN 100 ")
primes_c1 = [x for x in range(1, LIMIT + 1) if is_prime_c1(x)]
print(primes_c1, "\n")

is_prime_c2 = lambda n: n > 1 and sum(i for i in range(1, n + 1) if n % i == 0) == n + 1

print(" SỐ NGUYÊN TỐ TỪ 1 ĐẾN 100 ")
primes_c2 = [x for x in range(1, LIMIT + 1) if is_prime_c2(x)]
print(primes_c2, "\n")



is_prime_c3 = lambda n: n > 1 and not any(n % i == 0 for i in range(2, int(math.isqrt(n)) + 1))

print("  SỐ NGUYÊN TỐ TỪ 1 ĐẾN 100 ")
primes_c3 = [x for x in range(1, LIMIT + 1) if is_prime_c3(x)]
print(primes_c3, "\n")


def F(k):
    if k <= 1:
        return False
   
    uoc_so = list(filter(lambda i: k % i == 0, range(1, k + 1)))
   
    return len(uoc_so) == 2

print(" (Hàm def F): SỐ NGUYÊN TỐ TỪ 1 ĐẾN 100 ")
primes_c4 = [x for x in range(1, LIMIT + 1) if F(x)]
print(primes_c4)