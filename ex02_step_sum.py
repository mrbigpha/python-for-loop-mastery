def step_sum(start, end, step):
    """
    คำอธิบาย:
    หาผลรวมของตัวเลขตั้งแต่ start ถึง end (รวม end ถ้าอยู่ในลำดับ)
    โดยเพิ่มค่าทีละ step โดยใช้ range(start, stop, step)
    
    พารามิเตอร์:
    start (int): จุดเริ่มต้น
    end (int): จุดสิ้นสุด
    step (int): ระยะห่างของการเพิ่มค่า
    
    ผลลัพธ์:
    int: ผลรวมของตัวเลขในลำดับ
    
    ตัวอย่าง:
    step_sum(1, 10, 2) -> 1 + 3 + 5 + 7 + 9 = 25
    step_sum(2, 10, 3) -> 2 + 5 + 8 = 15
    """
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    total = sum(range(start, end + 1,step))
    return total
    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    # ทดสอบด้วยตัวเอง
    try:
        result = step_sum(1, 10, 2)
        print(f"Test Case 1: step_sum(1, 10, 2) = {result} (คาดหวัง: {repr(25)})")
    except NotImplementedError:
        print(f"Test Case 1: step_sum(1, 10, 2) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 1: step_sum(1, 10, 2) = 💥 เกิดข้อผิดพลาด: {e}")
    try:
        result = step_sum(2, 10, 3)
        print(f"Test Case 2: step_sum(2, 10, 3) = {result} (คาดหวัง: {repr(15)})")
    except NotImplementedError:
        print(f"Test Case 2: step_sum(2, 10, 3) = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 2: step_sum(2, 10, 3) = 💥 เกิดข้อผิดพลาด: {e}")
