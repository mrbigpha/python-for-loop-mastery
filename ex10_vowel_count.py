def vowel_count(text):
    """
    คำอธิบาย:
    นับจำนวนสระ (a, e, i, o, u) ในข้อความ text (ไม่สนว่าเป็นพิมพ์เล็กหรือพิมพ์ใหญ่)
    
    พารามิเตอร์:
    text (str): ข้อความที่ต้องการตรวจสอบ
    
    ผลลัพธ์:
    int: จำนวนสระที่พบ
    
    ตัวอย่าง:
    vowel_count("hello world") -> 3 (e, o, o)
    vowel_count("Python") -> 1 (o)
    """
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count
    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    # ทดสอบด้วยตัวเอง
    try:
        result = vowel_count('hello world')
        print(f"Test Case 1: vowel_count('hello world') = {result} (คาดหวัง: {repr(3)})")
    except NotImplementedError:
        print(f"Test Case 1: vowel_count('hello world') = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 1: vowel_count('hello world') = 💥 เกิดข้อผิดพลาด: {e}")
    try:
        result = vowel_count('Python is fun')
        print(f"Test Case 2: vowel_count('Python is fun') = {result} (คาดหวัง: {repr(3)})")
    except NotImplementedError:
        print(f"Test Case 2: vowel_count('Python is fun') = 🚧 ยังไม่ได้เขียนโค้ด")
    except Exception as e:
        print(f"Test Case 2: vowel_count('Python is fun') = 💥 เกิดข้อผิดพลาด: {e}")
