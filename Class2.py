#Data Type
#1.int
age = 18
money = 200
zeroo = 0

print("---------")
print(type(money))
print(type(age))
print(type(zeroo))

#2. float
height = 175.8
profit = -0.9
zerooo = 0.0

print("----------")
print(type(height))
print(type(profit))
print(type(zerooo))

#3. bool
cat = True
dog = False
isCat = True

print("----------")
print(type(cat))
print(type(dog))
print(type(isCat))

#4. str
hello = "Hello world"
phone = "063"
tell = "I'm batman"

print("----------")
print(type(hello))
print(type(phone))
print(type(tell))


print("=====[ Tybe conversion ]=====")
# str -> int
abc = "100" #str
cba = 100 #int

int()
float()
str()

#print(abc + 50) -> "100" + 50 False

print(int(abc) + 50) # 100 + 50 True


print("----------")
# float -> int
jud = 12.8 #float
print("This is jud : ", jud) # float

print("This is jud : ", int(jud)) #int 12.8 -> 12


#exam
a = "120"
b = "180"
print("a + b =", int(a) + int(b)) # 120 + 180 = 300

#exam
x2 = "33.3"
print(type(x2)) # "---" = str

teddy = 15
print("teddy is", float(teddy)) # 15 -> 15.0

bear = "big bear"
# str -> int, float XXXXFalse

# int, float -> str 
number = 191
print("number is", str(number))
print(type(str(number)))


print("=====[ Operation ]=====")
# x, y -> operands
# +, -, *, / -> operator


# ======[+]======
print("------[+]------")
print(12 + 8) #20
#print("Hello" + 5) FalseXXXX
print("Hello + World :", "Hello" + "world")

# ======[-]======
print("------[-]------")
print(10 - 5) #5
print(2 - 200) #-198

# ======[*]======
print("------[*]------")
print(5 * 3)
print("Hello" * 3) #HelloHelloHello
print(200 * -2)

# ======[/]====== float///
print("------[/]------")
print(4 / 2) #2.0
print(10 / 3) 

#=======[%]====== เศษ
print("------[%]------")
print(4 % 2) # 4/2 = 2 %0
print(10 % 3) # 10/3 = 9 %1

#=======[**]====== 
print("------[**]------")
print(2 ** 3) # 2*2*2 -> 8


#========[ Compare Operator ]========
# == , != , > ,< , >= , <=

o1 = 5
o2 = 10

# == is equal
print("======[ = ]======")
print(o1 == 5) #True
#print(o1 == o2) FalseXXX -> 5 = 10?

# != not equal 
print("======[ != ]======")
print(o1 != 10)

# < >
print("======[ < ]=======")
print(o1 < o2)
print(o2 < -20)

print(o2 > 10)

# <= =>
print("======[ <= ]=======")
print(o1 >= 10)
print(o2 >= 10)



print("=======[ Boolean operator ]=======")
p = True
q = False

#and 
print(p and q) #False

#or
print(p or q) #True

#not
print(not q) #True



#whatUp = input("my name is :")
#print(whatUp)


#=========[ If ]========
print("=======[ If ]=======")
pton_is_itim = True #False -> nothing
if pton_is_itim:
    print("mai gin")

print("=======[ If else ]=======")
pton_aroi = False
if pton_is_itim and pton_aroi:
    print("mai gin")
else:
    print("mai gin too")

print("=======[ elif ]=======")
pton_cheap = True
if pton_is_itim and pton_aroi:
    print("mai gin")
elif pton_cheap:
    print("give to another")
else:
    print("mai gin too")







