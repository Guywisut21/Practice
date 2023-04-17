#Type conversation
x = 10
y = 3.14
z = "20"

#บวกเลข

print(type(x))
print(type(y))
print(type(z))

#บวกเลข
result = x+y
print(result)

#บวกเลขข้ามชนิด
print(x+int(z))

#บวกเลขผิดๆ
print(str(y)+z)

#test
print(int(y))

result2 = y+float(z)
print(result2)
print(type(result2))

#แปลงค่าไม่ได้หากไม่ Operate
float(z)
print(type(z))

#Operate ค่าภายหลังจะแปลงได้
v="50"
v=float(v)
print(v)
print(type(v))