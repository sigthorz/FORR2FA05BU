import random
import time
import sys
from HermadurCLASS import *

#Afsakið ég hélt ég hefði sett skjalið sem zip í innu

def delay(i):
    for x in i:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.1)
def slightDelay(i):
    for x in i:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.1)


delay("_____________Byrjun_____________")
print("  ")
þinætt = input("Pessar, Hettar og Dreyar eru í stríði. Hvaða ætt tilheyrir þú? ")
print("  ")

if þinætt == "Hettar" or "HETTAR" or "hettar":
    delay("Þú hefur valið Hetta")
    print("  ")
elif þinætt == "Pessar" or "PESSAR" or "pessar":
    delay("Þú hefur valið Pessa")
    print("  ")
elif þinætt == "Dreyrar" or "DREYRAR" or "dreyrar":
    delay("Þú hefur valið Dreyra")
time.sleep(0.2)

print("  ")

delay("____________________________Reglurnar____________________________")
print("  ")
delay("Nú færð þú að ráða, hvað allar ættir fá að nota marga hermenn")
print("  ")


delay("Hversu margir Pessa hermenn eiga að fá að berjast? ")
print("  ")
nafn = "Pessi"
pe=int(input("Sláðu það inn hér: "))
pessi = aettbalkar(nafn,pe)


delay("Hversu margir Dreyra hermenn eiga að fá að berjast? ")
print("  ")
nafn="Dreyri"
dr=int(input("Sláðu það inn hér: "))
dreyri = aettbalkar(nafn,dr)


delay("og að lokum, hversu margir Hatta hermenn eiga að fá að berjast? ")
print("  ")
nafn="Höttur"
ho=int(input("Sláðu það inn hér: "))
hottur = aettbalkar(nafn,ho)
print(".")
time.sleep(0.2)
print("..")
time.sleep(0.1)
print("...")
time.sleep(0.2)

print("________________________________________________________")
delay("Hver hermaður hefur eitt vopn, mis mikið af lífi, og afl")
print("  ")
time.sleep(0.5)

delay("Vopn getur verið Sverð með aflið 1, Spjót með aflið 2 og Exi með aflið 3")
print("  ")
time.sleep(2)

delay("Hermaður getur verið með 1-5 líf, og ef hann missir þau öll þá deyr hann")
print("  ")
time.sleep(2)

delay("Hermaður getur einungis verið mis sterkur, stirkleiki er á bilinu 1-5")
print("  ")
time.sleep(2)

delay("Hermenn berjast í einvígi")
print("  ")
time.sleep(0.6)

delay("Ef hermennirnir sem eru að berjast eru með eins vopn og jafn sterkir þá missa þeir báðir eitt líf")
print("  ")
time.sleep(3)

delay("Nú ættir þú að skilja þetta, þá skulum við byrja")
print("  ")
time.sleep(0.5)
print()
print(".")
time.sleep(0.3)
print("..")
time.sleep(0.4)
print("...")
time.sleep(0.5)

slightDelay("____________________________")
time.sleep(0.5)
delay("BARDAGI EITT")
time.sleep(0.5)
slightDelay("____________________________")
print("  ")

pessar = pessi
dreyrar = dreyri
hettir = hottur
leiknr=1
on = True

while on == True: 
    delay("Fjöldi hermanna í hverju liði: ")
    print("  ")
    
    slightDelay("____________________________")
    print("  ")
    print("Leykur númer",leiknr,"er að hefjast")
    print("  ")
    print("Fjöldi hermanna í Pessar: ",len(pessar))
    print("  ")
    print("Fjöldi hermanna í Dreyrar: ",len(dreyrar))
    print("  ")
    print("Fjöldi hermanna í Höttum: ",len(hettir)) 
    slightDelay("____________________________")
    print("  ")
    slightDelay("____________________________")
    print("  ")
    print("Pessar")
    print("  ")

    for x in pessar:
        print(x)
        print("  ")
        time.sleep(3)

    print("Dreyrar")
    print("  ")
    for c in dreyrar:
        print(c)
        print("  ")
        time.sleep(3)

    print("Hettir")
    print("  ")
    for v in hettir:
        print(v)
        print("  ")
        time.sleep(4)

    leiknr+=1
    slightDelay("____________________________")
    print("  ")
    print("Nú færð þú sem foringi ættarinnar",þinætt,", að ráða hvaða hermenn eiga að berjast hér og nú.")
    print("  ")
    time.sleep(0.1)
    delay("Hvaða hermadur úr Pessa listanum hér að ofan á að fara fyrir hönd Pessa?")
    print("  ")
    Phermadur=int(input("Sláðu það inn hér: "))
    print("  ")
    print("  ")
    delay("Hvaða hermadur úr Pessa listanum hér að ofan á að fara fyrir hönd Pessa?")
    print("  ")
    Dhermadur=int(input("Sláðu það inn hér: "))
    print("  ")
    print("  ")
    delay("Hvaða hermadur úr Pessa listanum hér að ofan á að fara fyrir hönd Pessa?")
    print("  ")
    Hhermadur=int(input("Sláðu það inn hér: "))
    slightDelay("____________________________")
    print("  ")
    slightDelay("____________________________")
    print("  ")

    if len(pessar)> 0:
        if len(pessar)>=Phermadur-1:
            p=pessar.pop(Phermadur-1)
        else:
            p=pessar.pop(random.randint(0,len(pessar)-1))
        time.sleep(0.5)
    if len(dreyrar)> 0:
        if len(dreyrar)>=Dhermadur-1:
            d=dreyrar.pop(Dhermadur-1)
        else:
            d=dreyrar.pop(random.randint(0,len(dreyrar)-1))
        time.sleep(0.5)
    if len(hettir)> 0:
        if len(hettir)>=Hhermadur-1:
            h=hettir.pop(Hhermadur-1)
        else:
            h=hettir.pop(random.randint(0,len(hettir)-1))
        time.sleep(0.5)
    slightDelay("____________________________")
    print("  ")
    listi=[p,d,h]
    if len(pessar)==0:
        listi.remove(p)
    elif len(dreyrar)==0:
        listi.remove(d)
    elif len(hettir)==0:
        listi.remove(h)
    lid1=random.choice(listi)
    time.sleep(0.5)
    if lid1.aettbalkur=="Pessi":
        listi.remove(p)
        delay("Pessi!")
        print("  ")
        time.sleep(0.5)
    elif lid1.aettbalkur=="Dreyri":
        delay("Dreyri!")
        print("  ")
        listi.remove(d)
    elif lid1.aettbalkur=="Höttur":
        delay("Hettir!")
        print("  ")
        listi.remove(h)
    lid2=random.choice(listi)
    print("  ")
    slightDelay("______________________")
    print("  ")
    if lid1.aettbalkur == "Pessi" and lid2.aettbalkur == "Dreyri" or lid2.aettbalkur == "Pessi" and lid1.aettbalkur == "Dreyri":
        if len(hettir)>0:
            delay("Hettir!!")
            hettir.append(h)
    elif lid1.aettbalkur == "Pessi" and lid2.aettbalkur == "Höttur" or lid2.aettbalkur == "Pessi" and lid1.aettbalkur == "Höttur":
        if len(dreyrar)>0:
            delay("Dreyrar!!")
            dreyrar.append(d)
    elif lid1.aettbalkur == "Dreyri" and lid2.aettbalkur == "Höttur" or lid2.aettbalkur == "Dreyri" and lid1.aettbalkur == "Höttur":
        if len(pessar)>0:
            delay("Pessar!!")
            pessar.append(p)   
    print(lid1)
    print(lid2)
    time.sleep(0.5)
    print("  ")

    if lid1.vopn+1 + lid1.afl > lid2.afl + lid2.vopn+1:
        print("lið 1!!")
        if lid1.aettbalkur=="Pessi":
            pessar.append(p)
            print("Pessi, 1")
        elif lid1.aettbalkur=="Dreyri":
            dreyrar.append(d)
            print("Dreyri, 1")
        elif lid1.aettbalkur=="Höttur":
            hettir.append(h)
            print("Hettur, 1")
        if lid2.lif==1:
            print(lid2,"Hermaður féll.")
        else:
            lid2.lif=lid2.lif-1
            if lid2.aettbalkur=="Pessi":
                pessar.append(p)
                print("Pessi, 2")
            elif lid2.aettbalkur=="Dreyri":
                dreyrar.append(d)
                print("Dreyri, 2")
            elif lid2.aettbalkur=="Höttur":
                hettir.append(h)
                print("Hettur, 2")
        slightDelay("____________________")
        print("  ")
    elif lid1.vopn+1 + lid1.afl < lid2.afl + lid2.vopn+1:
        print("lið 2")
        if lid2.aettbalkur=="Pessi":
            pessar.append(lid2)
            print("Pessi, 3")
        elif lid2.aettbalkur=="Dreyri":
            dreyrar.append(lid2)
            print("Dreyri, 3")
        elif lid2.aettbalkur=="Höttur":
            hettir.append(lid2)
            print("Hettur, 3")
        if lid1.lif==1:
            print(lid1,"Hermaður féll.")
        elif lid1.lif>=2:
            lid1.lif=lid1.lif-1
            if lid1.aettbalkur=="Pessi":
                pessar.append(lid1)
                print("Pessi, 4")
            elif lid1.aettbalkur=="Dreyri":
                dreyrar.append(lid1)
                print("Dreyri, 4")
            elif lid1.aettbalkur=="Höttur":
                hettir.append(lid1)
                print("Hettur, 4")
    else:
        if lid1.lif==1 or lid2.lif==1:
            print(lid1,"og",lid2,"hermenn dóu")
        if lid1.lif>=2:
            print("1")
            lid1.lif=lid1.lif-1
            if lid1.aettbalkur=="Pessi":
                pessar.append(lid2)
                print("Pessi, 5")
            elif lid1.aettbalkur=="Dreyrar":
                dreyrar.append(lid2)
                print("Dreyri, 5")
            elif lid1.aettbalkur=="Hettir":
                hettir.append(lid2)
                print("Hettur, 5")
            slightDelay("_______________________")
            print("  ")
        if lid2.lif>=2:
            lid2.lif=lid2.lif-1
            print("2")
            if lid2.aettbalkur=="Pessi":
                pessar.append(p)
                print("Pessi, 6")
            elif lid2.aettbalkur=="Dreyri":
                dreyrar.append(d)
                print("Dreyri, 6")
            elif lid2.aettbalkur=="Höttur":
                hettir.append(h)
                print("Hettur, 6")
    slightDelay("____________________________")

    print("  ")
    if len(pessar)==0 and len(dreyrar)==0:
        delay("HETTAR ættin vann")
        n = False
    elif len(pessar)==0 and len(hettir)==0:
        print("DREYRA ættin vann")
        on = False
    elif len(hettir)==0 and len(dreyrar)==0:
        delay("PESSA ættin vann")
        on = False
    elif len(hettir)==0 and len(dreyrar)==0 and len(pessar)==0:
        delay("Það er jafntefli")
        on = False
    else:
        pass


print("  ")
print("Fjöldi hermanna í Pessar: ",len(pessar))
print("Fjöldi hermanna í Dreyrar: ",len(dreyrar))
print("Fjöldi hermanna í Höttum: ",len(hettir))


