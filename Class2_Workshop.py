x1 = 10
x2 = 15
x3 = 25  # ไม่ต้องตั้ง พิมพ์เลย
x4 = 35
x5 = 45


kilo = int(input("โปรแกรมคำนวณค่าขนส่ง โปรดใส่ระยะทาง : "))


if kilo >=0 and kilo <= 5:  # kilo <5
    print("ไม่สามารถจัดส่งได้")
elif kilo >= 5 and kilo <=50:  # kilo <=50
    print("ต้องจ่ายค่าขนส่ง :", x1, "บาท")
elif kilo >= 51 and kilo <=100:  # kilo <=100
    print("ต้องจ่ายค่าขนส่ง :", x2, "บาท")
elif kilo >= 101 and kilo <=300:  # kilo <=300
    print("ต้องจ่ายค่าขนส่ง :", x3, "บาท")
elif kilo >= 301 and kilo <=500:  # kilo <=500 
    print("ต้องจ่ายค่าขนส่ง :", x4, "บาท")
else:
    print("ต้องจ่ายค่าขนส่ง :", x5, "บาท")