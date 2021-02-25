#Sigþór Atli Sverrisson
import math
# <--- Klassar byrja --->

#Liður 1 - Hringur
class Hringur():
    def __init__(self, radius):
        self.radius = radius

    def reikna_ummal(self):
        #Reiknar Ummál hrings
        utkoma = (2 * math.pi * self.radius)
        return round (utkoma,1)

    def reikna_flatarmal(self):
        #Reiknar Flatarmál hrings
        utkoma = (math.pi * (self.radius ** 2))
        return round (utkoma,1)

    def reikna_rummal(self):
        #Reiknar Rúmmál hrings
        utkoma = (4.0/3.0) * math.pi * (self.radius ** 3)
        return round (utkoma, 1)

#Liður 2 - Bankareikningur
class Eigandi():
    def __init__(self,n,i):
        self.nafn=n
        self.upphaed=i

    def __str__(self):
        return self.nafn+": "+str(self.upphaed)

    #Checkar hvort það er nógu mikill pening inn í reikningum og tekur út úr honum
    def uttekt(self,upph):
        if self.upphaed >= upph:
            self.upphaed=self.upphaed-upph
        else:
            print("þú ert ekki með nóg á reikningnum þínum")

    #Bætir við upphæðina
    def innlogn(self,upphaed):
        self.upphaed = self.upphaed + upphaed

#Liður 3 - Nemendur
class Nemi:
    def __init__(self,n,a):
        self.nafn=n
        self.aldur=a

def nemendur():
    nemlisti=[]
    for x in range(5):
        nafnnem=input("Sláðu in nafn nemanda: ")
        aldurnem=int(input("Sláðu inn aldur nemanda: "))
        n = Nemi(nafnnem,aldurnem)
        nemlisti.append(n)
    return nemlisti

def finnaMedaltal(listi):
    summa = 0
    for i in listi:
        summa += i.aldur
    medaltal=summa/5
    print ("\n")
    print ("Meðalaldur nemanda er:", round(medaltal))

# <--- Klassar enda --->

# <--- Föll utan klasa byrja --->

def prenta_reikninga(listi):
    for x in eigandalisti:
        print(x)

def eyda(listi,nafn):
    stadur=0
    #For loopa til að finna staðsetningu reiknings
    for x in range(len(listi)):
        if listi[x].nafn == nafn:
            stadur=x
    #tekur niðurstöðu og poppar(eyðir) úr listanum
    listi.pop(stadur)
    return listi

# <--- Föll utan klasa enda --->

on = 1
while on == 1:
    print ("1. Hringur")
    print ("2. Bankareikningur/Skráarvinnsla")
    print ("3. Nemendur")
    print ("4. Hætta")
    val = int(input("Hvað villt þú gera: "))

    #Liður 1 - Hringur
    if val == 1:
        off = 1
        while off == 1:
            print ("1. Ummál")
            print ("2. Flatarmál")
            print ("3. Rúmmál")
            val = int(input("Hvað villt þú gera: "))

            radius = int(input("Hver er radíus hringsins? "))
            r1 = Hringur(radius)
            #Kallar á viðeigandi fall
            if val == 1:
                print("Ummálið hringsins þíns er:",r1.reikna_ummal())

            elif val == 2:
                print ("Flatarmál hringsing þíns er:", r1.reikna_flatarmal())

            elif val == 3:
                print ("Rúmmál hringsins þín er:", r1.reikna_rummal())

            elif val == 4:
                off = 0
            else:
                print ("Þú hefur valið eitthvað rangt")
    #Liður 2 - Bankareikningur
    elif val == 2:
        eigandalisti = [Eigandi("Jonas", 1000),Eigandi("Tumi",3500),Eigandi("Tommi", 500),Eigandi("Dagur",800),Eigandi("Halldór",642)]
        for x in eigandalisti:
            print(x)

        lidur2=1
        while lidur2==1:
            print("1. Nýr reikningur")
            print("2. Taka út úr reikning")
            print("3. Leggja inn á reikning")
            print("4. Eyða reikning")
            print("5. Birta alla reikninga")
            print("6. Hætta")
            val = int(input("Hvað vilt þú gera? "))

            if val ==1:
                #Fær nafn og upphæð nýs reiknins
                nafn=input("Sláðu inn nafn reikningshafa: ")
                upphh=int(input("Sláðu inn upphæð reiknings:"))
                e1=Eigandi(nafn,upphh)
                #Bætir inn í lista
                eigandalisti.append(e1)
                for x in eigandalisti:
                    print(x)

            elif val==2:
                #Fær nafn og upphæð til að taka út af og kalla á fallið uttekt í klasanum Eigandi
                nafnut=input("Sláðu inn nafn reikningshafa: ")
                upput=int(input("Hversu mikið viltu taka út: "))
                for x in eigandalisti:
                    if x.nafn == nafnut:
                        x.uttekt(upput)
                for x in eigandalisti:
                    print(x)

            elif val ==3:
                #Fær nafn reiknings og hversu mikið er lagt inn á hann, kallar á fallið upphaed í klasanum Eigandi
                nafnut = input("Sláðu inn nafn reikningshafa: ")
                upphaed = int(input("Hversu mikið viltu leggja inn? "))
                for x in eigandalisti:
                    if x.nafn == nafnut:
                        x.innlogn(upphaed)
                    for x in eigandalisti:
                        print(x)

            elif val==4:
                #Fær nafn reiknings og kallar á fall til að eyða reikningi
                nafn=input("Sláðu inn nafn reiknings sem þú villt eyða: ")
                eigandalisti=eyda(eigandalisti,nafn)
                for x in eigandalisti:
                    print(x)

            elif val==5:
                #Kalla á fall til að prenta
                eigandalisti=prenta_reikninga(eigandalisti)

            elif val ==6:
                lidur2=0

            else:
                print ("Þú hefur valið eitthvað rangt")

    #Liður 3 - Nemendur
    elif val == 3:
        l=nemendur()
        finnaMedaltal(l)

    #Valmynd hættir
    elif val == 4:
        on = 0
    else:
        print ("Þú hefur valið eitthvað rangt")
