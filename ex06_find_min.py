def find_min(numbers):
    """
    คำอธิบาย:
    หาค่าที่น้อยที่สุดในลิสต์ numbers ห้ามใช้ฟังก์ชัน min()
    
    พารามิเตอร์:
    numbers (list): ลิสต์ของจำนวนเต็ม
    
    ผลลัพธ์:
    int: ค่าที่น้อยที่สุด
    
    ตัวอย่าง:
    find_min([10, 5, 8, 2, 7]) -> 2
    """
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    min_val = numbers[0]
    for i in numbers:
        if i < min_val:
            min_val = i
    return min_val
    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    # ทดสอบด้วยตัวเอง
    try:
        result = find_min([10, 5, 8, 2, 7])
        print(f"Test Case 1: find_min([10, 5, 8, 2, 7]) = {result} (คาดหวัง: {repr(2)})")
    except NotImplementedError:
        print(f"Test Case 1: find_min([10, 5, 8, 2, 7]) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 1: find_min([10, 5, 8, 2, 7]) = 💥 เกิดข้อผิดพลาด: {e}")
    try:
        result = find_min([1])
        print(f"Test Case 2: find_min([1]) = {result} (คาดหวัง: {repr(1)})")
    except NotImplementedError:
        print(f"Test Case 2: find_min([1]) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 2: find_min([1]) = 💥 เกิดข้อผิดพลาด: {e}")
