def reverse_string(text):
    """
    คำอธิบาย:
    กลับด้านข้อความ text โดยใช้ for loop (ห้ามใช้ text[::-1])
    
    พารามิเตอร์:
    text (str): ข้อความที่ต้องการกลับด้าน
    
    ผลลัพธ์:
    str: ข้อความที่กลับด้านแล้ว
    
    ตัวอย่าง:
    reverse_string("hello") -> "olleh"
    """
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    result = ""
    for char in text:
        result = char + result  # วางตัวอักษรใหม่ไว้หน้าสุดเสมอ
    return result
    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    # ทดสอบด้วยตัวเอง
    try:
        result = reverse_string('hello')
        print(f"Test Case 1: reverse_string('hello') = {result} (คาดหวัง: {repr(olleh)})")
    except NotImplementedError:
        print(f"Test Case 1: reverse_string('hello') = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 1: reverse_string('hello') = 💥 เกิดข้อผิดพลาด: {e}")
    try:
        result = reverse_string('Python')
        print(f"Test Case 2: reverse_string('Python') = {result} (คาดหวัง: {repr(nohtyP)})")
    except NotImplementedError:
        print(f"Test Case 2: reverse_string('Python') = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 2: reverse_string('Python') = 💥 เกิดข้อผิดพลาด: {e}")