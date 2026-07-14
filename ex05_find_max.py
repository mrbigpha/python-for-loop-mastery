def find_max(numbers):
    """
    คำอธิบาย:
    หาค่าที่มากที่สุดในลิสต์ numbers โดยใช้ for loop ห้ามใช้ฟังก์ชัน max()
    
    พารามิเตอร์:
    numbers (list): ลิสต์ของจำนวนเต็ม (มีสมาชิกอย่างน้อย 1 ตัว)
    
    ผลลัพธ์:
    int: ค่าที่มากที่สุดในลิสต์
    
    ตัวอย่าง:
    find_max([1, 5, 3, 9, 2]) -> 9
    find_max([-1, -5, -2]) -> -1
    """
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    max_val = numbers[0]
    for i in numbers:
        if i > max_val:
            max_val = i
    return max_val
    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    # ทดสอบด้วยตัวเอง
    try:
        result = find_max([1, 5, 3, 9, 2])
        print(f"Test Case 1: find_max([1, 5, 3, 9, 2]) = {result} (คาดหวัง: {repr(9)})")
    except NotImplementedError:
        print(f"Test Case 1: find_max([1, 5, 3, 9, 2]) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 1: find_max([1, 5, 3, 9, 2]) = 💥 เกิดข้อผิดพลาด: {e}")
    try:
        result = find_max([-1, -5, -2])
        print(f"Test Case 2: find_max([-1, -5, -2]) = {result} (คาดหวัง: {repr(-1)})")
    except NotImplementedError:
        print(f"Test Case 2: find_max([-1, -5, -2]) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 2: find_max([-1, -5, -2]) = 💥 เกิดข้อผิดพลาด: {e}")
