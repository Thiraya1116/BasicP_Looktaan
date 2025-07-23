#เลือดศัตรู
slime = 120

#อาวุธ 3 อย่าง

sword = 25
bow = 20
knife = 10

#loop ให้เลือก 1สู้ 2หนี
while True:
    print("อันตราย!! คุณได้เจอเข้ากับ Slime (HP. 120) คุณจะทำอย่างไรต่อไป?")
    print("1.ต่อสู้")
    print("2.หนี")
    select = int(input("กรุณาเลือก 1 หรือ 2 :"))
    if select == 1:
        print("คุณได้เลือกที่จะต่อสู้ อาวุธที่คุณจะเลือกต่อสู้ได้มีดังนี้")
        print("1.ดาบ (Dmg. = 25)")
        print("2.ธนู (Dmg. = 20)")
        print("3.มีดสั้น (Dmg. = 10)")
        round = int(input("คุณเลือกที่จะตีกี่รอบ :"))
        weapon = input("กรุณาเลือกอาวุธ :")
        if weapon == 1:
            slime -= sword
            print("คุณโจมตี Slime ไป", sword, "ดาเมจ HP.คงเหลือ", slime)
            if slime == 0:
                print("คุณกำจัด Slime ได้แล้ว")
                break
        elif weapon == 2:
            slime -= bow
            print("คุณโจมตี Slime ไป", bow, "ดาเมจ HP.คงเหลือ", slime)
            if slime == 0:
                print("คุณกำจัด Slime ได้แล้ว")
                break
        elif weapon == 3:
            slime -= knife
            print("คุณโจมตี Slime ไป", knife, "ดาเมจ HP.คงเหลือ", slime)
            if slime == 0:
                print("คุณกำจัด Slime ได้แล้ว")
                break    
    elif select == 2:
        print("คุณเลือกที่จะหนี เสียใจด้วยการผจญภัยของคุณจบลงแล้ว")
        break
