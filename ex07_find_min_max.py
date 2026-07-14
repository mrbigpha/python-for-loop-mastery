def find_min_max(numbers):
    """
    คำอธิบาย:
    หาทั้งค่าที่น้อยที่สุด และค่าที่มากที่สุดในลิสต์ numbers พร้อมกัน
    ให้คืนค่าเป็น tuple (min_value, max_value)
    
    พารามิเตอร์:
    numbers (list): ลิสต์ของจำนวนเต็ม (มีสมาชิกอย่างน้อย 1 ตัว)
    
    ผลลัพธ์:
    tuple: (ค่าที่น้อยที่สุด, ค่าที่มากที่สุด)
    
    ตัวอย่าง:
    find_min_max([1, 5, 3, 9, 2]) -> (1, 9)
    find_min_max([10]) -> (10, 10)
    """
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    minv = numbers[0]
    maxv = numbers[0]

    for i in numbers:
        if i < minv:
            minv = i
        if i > maxv:
            maxv = i
    return (minv, maxv)
    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    # ทดสอบด้วยตัวเอง
    try:
        result = find_min_max([1, 5, 3, 9, 2])
        print(f"Test Case 1: find_min_max([1, 5, 3, 9, 2]) = {result} (คาดหวัง: {repr((1, 9))})")
    except NotImplementedError:
        print(f"Test Case 1: find_min_max([1, 5, 3, 9, 2]) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 1: find_min_max([1, 5, 3, 9, 2]) = 💥 เกิดข้อผิดพลาด: {e}")
    try:
        result = find_min_max([10])
        print(f"Test Case 2: find_min_max([10]) = {result} (คาดหวัง: {repr((10, 10))})")
    except NotImplementedError:
        print(f"Test Case 2: find_min_max([10]) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 2: find_min_max([10]) = 💥 เกิดข้อผิดพลาด: {e}")
