def calculate_factorial(n):
    """
    คำอธิบาย:
    คำนวณค่าแฟกทอเรียล (n!) โดยที่ n! = n * (n-1) * (n-2) * ... * 1
    กำหนดให้ 0! = 1
    
    พารามิเตอร์:
    n (int): จำนวนเต็มบวกหรือศูนย์
    
    ผลลัพธ์:
    int: ค่าแฟกทอเรียลของ n
    
    ตัวอย่าง:
    calculate_factorial(5) -> 120
    calculate_factorial(0) -> 1
    """
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    # ทดสอบด้วยตัวเอง
    try:
        result = calculate_factorial(5)
        print(f"Test Case 1: calculate_factorial(5) = {result} (คาดหวัง: {repr(120)})")
    except NotImplementedError:
        print(f"Test Case 1: calculate_factorial(5) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 1: calculate_factorial(5) = 💥 เกิดข้อผิดพลาด: {e}")
    try:
        result = calculate_factorial(3)
        print(f"Test Case 2: calculate_factorial(3) = {result} (คาดหวัง: {repr(6)})")
    except NotImplementedError:
        print(f"Test Case 2: calculate_factorial(3) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 2: calculate_factorial(3) = 💥 เกิดข้อผิดพลาด: {e}")
