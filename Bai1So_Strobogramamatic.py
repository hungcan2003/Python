def laStrobogrammatic(s):

    doi = {
        '0': '0',
        '1': '1',
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

def main():
    n = input("Nhap so: ")
    if laStrobogrammatic(n):
        print(n, "la so strobogrammatic")
    else:
        print(n, "khong phai la so strobogrammatic")

main()