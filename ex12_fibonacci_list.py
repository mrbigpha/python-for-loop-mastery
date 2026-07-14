def fibonacci_list(n):
    """
    คำอธิบาย:
    สร้างลิสต์ของลำดับฟีโบนัชชี n ตัวแรก
    ลำดับฟีโบนัชชีคือลำดับที่ตัวถัดไปเกิดจากผลรวมของ 2 ตัวก่อนหน้า
    เริ่มด้วย 0 และ 1 (เช่น 0, 1, 1, 2, 3, 5, 8, ...)
    
    พารามิเตอร์:
    n (int): จำนวนตัวที่ต้องการในลำดับ (n >= 1)
    
    ผลลัพธ์:
    list: ลิสต์ของลำดับฟีโบนัชชี
    
    ตัวอย่าง:
    fibonacci_list(5) -> [0, 1, 1, 2, 3]
    fibonacci_list(1) -> [0]
    """
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    fib = [0]
    if n == 1:
        return fib

    fib.append(1)
    for i in range(2, n):
        next_num = fib[i-1] + fib[i-2]
        fib.append(next_num)
    return fib
    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    # ทดสอบด้วยตัวเอง
    try:
        result = fibonacci_list(5)
        print(f"Test Case 1: fibonacci_list(5) = {result} (คาดหวัง: {repr([0, 1, 1, 2, 3])})")
    except NotImplementedError:
        print(f"Test Case 1: fibonacci_list(5) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 1: fibonacci_list(5) = 💥 เกิดข้อผิดพลาด: {e}")
    try:
        result = fibonacci_list(1)
        print(f"Test Case 2: fibonacci_list(1) = {result} (คาดหวัง: {repr([0])})")
    except NotImplementedError:
        print(f"Test Case 2: fibonacci_list(1) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 2: fibonacci_list(1) = 💥 เกิดข้อผิดพลาด: {e}")
