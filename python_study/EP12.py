# โปรแกรมคำนวณค่า BMI (ดัชนีมวลกาย)
# BMI = น้ำหนัก (kg) / ส่วนสูง * ส่วนสูง (m)

# Input / convert to integer
weight=int(input("ป้อนน้ำหนักของคุณ (kg) : "))
high=int(input("ป้อนส่วนสูงของคุณ (cm) : "))/100
#output
print("BMI = ",weight/(high**2))