def countdown(n):
    """
    คำอธิบาย:
    สร้างลิสต์ของตัวเลขถอยหลังตั้งแต่ n จนถึง 1 โดยใช้ range(start, stop, step)
    ที่มีค่า step เป็นลบ
    
    พารามิเตอร์:
    n (int): จุดเริ่มต้นของการถอยหลัง
    
    ผลลัพธ์:
    list: ลิสต์ของตัวเลขถอยหลัง [n, n-1, ..., 1]
    
    ตัวอย่าง:
    countdown(5) -> [5, 4, 3, 2, 1]
    countdown(3) -> [3, 2, 1]
    """
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    return list(range(n,0,-1))
    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    # ทดสอบด้วยตัวเอง
    try:
        result = countdown(5)
        print(f"Test Case 1: countdown(5) = {result} (คาดหวัง: {repr([5, 4, 3, 2, 1])})")
    except NotImplementedError:
        print(f"Test Case 1: countdown(5) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 1: countdown(5) = 💥 เกิดข้อผิดพลาด: {e}")
    try:
        result = countdown(3)
        print(f"Test Case 2: countdown(3) = {result} (คาดหวัง: {repr([3, 2, 1])})")
    except NotImplementedError:
        print(f"Test Case 2: countdown(3) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 2: countdown(3) = 💥 เกิดข้อผิดพลาด: {e}")
