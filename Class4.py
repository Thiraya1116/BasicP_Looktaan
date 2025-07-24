# ========[ Function ]========
def Hello():
    print("Hello World")

Hello()
# Hello()
# Hello()
# Hello()


#=========[ Parameters & Arguments ]==========
#ตัวแปร รับ & ส่งค่า

# Parameters
def add(x,yasd):
    print(x+yasd)

# Arguments
add(1,2)
add(7,4)
add(114,6)

a = 3
b = 35
add(a,b)


def introduction(name):
    print("My name is", name)
    # tellAge()

def tellAge():
    age = input(">> โปรดกรอกอายุของคุณ :")
    print("คุณอายุ", age, "ปี")


introduction("Looktaan")
# introduction("Pon")
# introduction("Naming")
# introduction("Da")
# introduction("Tonnam")

# tellAge()

def spam(K):
    r = int(input("วนกี่รอบ :"))
    for i in range(1,r+1):
        print("รอบที่", i, ":", K)

# spam("Looktaan")


def araiwa(c,d):
    return c+d #คิดแล้วแต่ไม่แสดงผล

#=====
print(araiwa(2,3))

#=====
m = 13
n = 16
result = araiwa(m,n)
print("result :", result)


#=========[ Data Structure ]========

# List
x = ["Looktaan", 1234, 8.9]  # 0, 1

print(x[1])

sum = x[1] + x[2]
print(sum)


x[1] = 234
sum = x[1] + x[2]
print(sum)

x[2] = "poo"
print(x)

# =================Appand===============
x.append("best")
x.append(90)
print(x)

a = 9
x.append(a)
print(x)


# ================Pop====================
# pop() -> ตัวสุดท้ายหาย
x.pop(2) # go to toilet
print(x) 
 
# ================for loop==============
for i in x:
    if i == 234:
        print(i)


# ==============Dictionary=============
dictGrade = {
    "A":80, # A = 80
    "B":70, # B = 70
    "C":60, # C = 60
}
print(dictGrade["A"])

dictGrade["A"] = 90  # แก้ไขข้อมูลที่มีอยู่แล้ว
print(dictGrade["A"])

dictGrade["D"] = 50 # เพิ่มข้อมูล
print(dictGrade["D"])


# ============Combination of DS================
students =  [
    {"name":"Looktaan", "id":49, "score":"A"},
    {"name":"Pton", "id":50, "score":"B"},
    {"name":"Tonnam", "id":67, "score":"A"},
]


for student in students:
    print(student["name"], student["id"], student["score"])

def checkMoney(list_of_students):
    for student in list_of_students:
        if student["money"] > 500:
            print("เงินมาก (มากกว่า 500)")
        else:
            print("เงินน้อย (น้อยกว่า 500)")

students =  [
    {"name":"Looktaan", "money":400},
    {"name":"Pton", "money":1000}
]

checkMoney(students)