def count_even(numbers):
    """
    คำอธิบาย:
    นับจำนวนเลขคู่ที่มีอยู่ในลิสต์ numbers โดยใช้ for loop
    
    พารามิเตอร์:
    numbers (list): ลิสต์ของจำนวนเต็ม
    
    ผลลัพธ์:
    int: จำนวนของเลขคู่
    
    ตัวอย่าง:
    count_even([1, 2, 3, 4, 5]) -> 2 (คือ 2 และ 4)
    count_even([2, 4, 6]) -> 3
    """
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    count = 0 
    for i in numbers:
        if i  % 2 == 0:
            count += 1
    return count
    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    # ทดสอบด้วยตัวเอง
    try:
        result = count_even([1, 2, 3, 4, 5])
        print(f"Test Case 1: count_even([1, 2, 3, 4, 5]) = {result} (คาดหวัง: {repr(2)})")
    except NotImplementedError:
        print(f"Test Case 1: count_even([1, 2, 3, 4, 5]) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 1: count_even([1, 2, 3, 4, 5]) = 💥 เกิดข้อผิดพลาด: {e}")
    try:
        result = count_even([2, 4, 6, 8])
        print(f"Test Case 2: count_even([2, 4, 6, 8]) = {result} (คาดหวัง: {repr(4)})")
    except NotImplementedError:
        print(f"Test Case 2: count_even([2, 4, 6, 8]) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 2: count_even([2, 4, 6, 8]) = 💥 เกิดข้อผิดพลาด: {e}")
