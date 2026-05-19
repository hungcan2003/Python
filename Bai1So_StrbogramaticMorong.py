def laStrobogrammatic(s):
    doi = {
        '0': '0',
        '1': '1',
        '2': '2',
        '5': '5',
        '8': '8',
        '6': '9',
        '9': '6'
    }
    left = 0
    right = len(s) - 1
    while left <= right:
        if s[left] not in doi:
            return False
        if doi[s[left]] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def laSoNguyenTo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    n = int(input("Nhap so: "))
    if laStrobogrammatic(str(n)) and laSoNguyenTo(n):
        print(n, "la so nguyen tosogrammatic")
    else:
        print(n, "khong phai")

main()