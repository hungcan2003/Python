is_phong_phu = lambda n: sum(i for i in range(1, (n // 2) + 1) if n % i == 0) > n


is_tang_dan = lambda n: list(str(n)) == sorted(str(n))


is_armstrong = lambda x: sum(int(d) ** len(str(x)) for d in str(x)) == x



if __name__ == "__main__":
    # Giới hạn quét từ 1 
    GH_TREN = 1000000
    
   
    
    print("--- KIỂM TRA ĐỘ CHÍNH XÁC CỦA CÁC HÀM LAMBDA ---")
    
    test_e = [x for x in range(1, 101) if is_phong_phu(x)]
    print(f"e.- Các số phong phú nhỏ hơn 100:\n{test_e}\n") 
    
    print(f"f.- Số 2345 có tăng dần không? {is_tang_dan(2345)}")
    print(f"    Số 5432 có tăng dần không? {is_tang_dan(5432)}\n")

    test_g = [x for x in range(1, GH_TREN + 1) if is_armstrong(x)]
    print(f"g.- Các số Armstrong nhỏ hơn 1 triệu tìm được:\n{test_g}")