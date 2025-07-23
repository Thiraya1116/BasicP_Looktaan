#=======[ conditions ]=======
# Nested condition

hasRice = True
hasSpoon = False

if hasRice:
    print("มีข้าว")
    if hasSpoon:
        print("มีช้อน")
        print("กินข้าว")
    else:
        print("กินข้าวไม่ได้ เพราะไม่มีช้อน")
    # print("OK")  #if1
else:
    print("กินข้าวไม่ได้ เพราะไม่มีข้าว")
    

#เล่นๆ

ticket = True
ticket_correct = False

if ticket:
    print("มีตั๋ว")
    if ticket_correct:
        print("ถูกต้อง")
        print("ขึ้นได้")
    else:
        print("ข้อมูลไม่ถูกต้อง")
        print("ขออภัย คุณไม่สามารถขึ้นได้")
    
else:
    print("ไม่มีตั๋ว")
    print("ขออภัย คุณไม่สามารถขึ้นได้")



#=======[ Loop ]========
print("===========[ Loop ]============")

# Range -> range(start, stop, step)
# range(1,10,2) -> [1,3,5,7,9]


# Loop for
for i in range(5):  # i = 0-4 -> 0 1 2 3 4
    print("Hello", i)

for i in range(1,5):  # i = 1-4 -> 1 2 3 4
    print("Bye", i)

for i in range(1,5,2):  # i = 1 3
    print("HI", i)


print("===========[ โปรมแกรมคำนวณผลรวม ]============")

box = 0
for i in range(5,10,2):
    print(box + i)
    # box = box + i
    box += i

print("ค่าของ box :", box) 


# print("===========[ การวนรอบ ]============")

#round = int(input("วนกี่รอบ :"))
# total = 0
# print("------------------")
# for i in range(1,round+1):
#     total += i
#     print("รอบที่", i, "ผลรวมคือ", total)
    


# While loop -> ทำงานไม่หยุด จนกว่าจะเจอ False

i = 0 
while i < 3:
    print("Hello") # o 1 2 -> Hello*3
    i += 1

# Break -> หยุด ลูป
i = 0
while i <= 5:
    print("Goodbye")
    i += 1
    if i > 10:
        break

while True:
    inp = float(input("input number:"))
    if inp == 7.0:
        break




