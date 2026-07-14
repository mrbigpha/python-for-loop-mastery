def multiplication_table(n):
    """
    คำอธิบาย:
    สร้างแม่สูตรคูณของแม่ n ตั้งแต่คูณ 1 ถึง 12 และเก็บผลลัพธ์ใส่ลิสต์
    
    พารามิเตอร์:
    n (int): แม่สูตรคูณที่ต้องการ
    
    ผลลัพธ์:
    list: ลิสต์ของผลคูณ (เช่น [n*1, n*2, ..., n*12])
    
    ตัวอย่าง:
    multiplication_table(2) -> [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
    """
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    result = []
    for i in range(1,13):
        result.append(n*i)
    return result
    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    # ทดสอบด้วยตัวเอง
    try:
        result = multiplication_table(2)
        print(f"Test Case 1: multiplication_table(2) = {result} (คาดหวัง: {repr([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])})")
    except NotImplementedError:
        print(f"Test Case 1: multiplication_table(2) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 1: multiplication_table(2) = 💥 เกิดข้อผิดพลาด: {e}")
    try:
        result = multiplication_table(5)
        print(f"Test Case 2: multiplication_table(5) = {result} (คาดหวัง: {repr([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])})")
    except NotImplementedError:
        print(f"Test Case 2: multiplication_table(5) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 2: multiplication_table(5) = 💥 เกิดข้อผิดพลาด: {e}")
