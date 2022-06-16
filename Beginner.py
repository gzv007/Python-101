# # ทดสอบการแสดงผล
# '''
# ฝึกการ
# เขียนโปรแกรม
# '''
# print("hello world")
# print(1)
# print(1.2)
# print(True)
# print(False)
# print("Supamongkol\t" + "Meechu") #\t = tab

#ตัวแปร
#ชื่อตัวแปร = ค่าที่เก็บ
# x = 20 #int
# y = "20" #str
# z = True #boolean
# print("ยอดเงินคงเหลือ " + str(x) +" บาท") #แปลง int to str
# print(int(y) + 40) #แปลง str to int
# print(type(z)) #หาชนิดตัวแปร

# #การตั้งชื่อตัวแปร
# '''
# 1.ห้ามขึ้นต้นด้วยตัวเลวหรือสัญลักษณ์พิเศษ
# 2.ห้ามซ้ำกับ Keyword (คำสงวน)
# 3.Case sensitive พิมพ์เล็กพิมพ์ใหญ่ มีความแตกต่าง
# '''

# รับข้อมูล input
# name = input("กรุณาป้อนชื่อ : ")
# age = input("กรุณาป้อนอายุ : ")
# print("ชื่อของคุณคือ : " + str(name) + " อายุ : " + str(age))    

# โปรแกรมคำนวณ BMI
# w = น้ำหนัก
# h = ส่วนสูง
# input
# w =  int(input("น้ำหนักของคุณ : "))
# h = int(input("ส่วนสูงของคุณ : "))
# # process
# h = h/100
# bmi = w/(h*h)
# # output
# print("ค่า BMI ของคุณคือ : "+ str(int(bmi)))

# การใช้ if 


score = int(input("คะแนนเท่าไหร่ : "))
# if score > 80 or score == 80  :
#     print("เกรด A")
# elif score >= 70 :
#     print("เกรด B")
# elif score >= 60 :
#     print("เกรด C")
# elif score >= 50 :
#     print("เกรด D")
# elif score < 50 :
#     print("เกรด E")

# Ternary operator
print("เกรด A") if score > 80 else print("จบ")