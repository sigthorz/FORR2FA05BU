import random
import csv

listi1 = []
listi2 = [2, 3, 5, 7, 11, 13, 17, 19]

def gera_lista(byrjun,endir,fjoldi = 100):
    for x in range(fjoldi):
        listi1.append(random.randint(byrjun,endir))
    return listi1

def syna_lista(listi):
    for x in range(len(listi)):
        if x == len(listi) - 1:
            print(listi[x])
        else:
            print(listi[x], end=":")

def medaltal(*tolur):
    summa = 0
    for x in tolur:
        summa += x
    summa = summa/len(tolur)
    summa = '{0:.3f}'.format(summa)
    return summa

def deilanlegt(tolulisti, tala):
    deilanlegt_Listi = []
    for q in tolulisti:
        if q // tala != 0:
            deilanlegt_Listi.append(q)
    return deilanlegt_Listi


gera_lista(100,200)
print("\nHérna er listinn með tvípunkti á milli hverri einustu tölu: \n")
syna_lista(listi1)
print("\nMeðaltal 7 talna\n")
print(medaltal(50,25,259,2,58,31,30))
print("\nMeðaltal 3 talna\n")
print(medaltal(75,79,47))
print(deilanlegt(listi2,2))


print("\nHérna eru öll nöfnin sem eru í skránni.\n")
with open('nemendur.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(f'{"".join(row)}')
        
    
nafn = input("\nsláðu inn nafn einstaklings: ")
with open('nemendur.csv', mode='a') as nemendur_file:
    nemendur_writer = csv.writer(nemendur_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    nemendur_writer.writerow([nafn])

print("\nHérna eru öll nöfnin sem eru í uppfærðu skránni.\n")
with open('nemendur.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(f'{"".join(row)}')
        


class Ferningur:
    def __init__(self,hlidA,hlidB):
        self.hlidA = hlidA
        self.hlidB = hlidB
    
    def __str__(self):
        return "blank"
    
    def staerri(self,ferningur2):
        return "blank"
