import csv
from random import randint, shuffle

def lesaSkra(nafntxt):
    with open(nafntxt) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        return list(csv_reader)


def spurning(spurningSvar):
    for x in range(2):
        notandi_svar=input(spurningSvar[0]+" ")
        if notandi_svar == spurningSvar[1]:
            print("RÉTT!")
            return True
    print("Rétta svarið er: "+spurningSvar[1])
    return False


def skrifaIskra(listi,nafntxt):
    with open(nafntxt, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(listi)


def lesaiSkra(nafntxt):
    with open(nafntxt, 'r') as f:
        reader = csv.reader(f)
        return list(reader)
    

def breytaUppl(simaskra,nafn,nyttGSM):
    ny_simaskra=simaskra
    with open('simaskra.csv','w+') as f:
        f.seek(0)
    for x in ny_simaskra:
        if x[0] == nafn:
            x[2] = nyttGSM
    for x in ny_simaskra:
        skrifaIskra(x,'simaskra.csv')


def eyda(simaskra,nafn):
    ny_simaskra = simaskra
    for x in ny_simaskra:
        if x != "": # if the line is not blank
            if x[0] == nafn: 
                ny_simaskra.remove(x)
    with open('simaskra.csv','w+') as f:
        f.seek(0)
    for x in ny_simaskra:
        skrifaIskra(x,'simaskra.csv')


def prenta(listi):
    for x in listi:
        print(', '.join(x))


val = int(input("-----Valmynd-----\n1.Spurningabanki\n2.Símaskrá\n3.Hætta\nSláðu inn val: "))
while val != 3:
    if val == 1:
        big_listi = lesaSkra('spurningar.csv')
        shuffle(big_listi)

        points = 0
        for x in big_listi:
            sp=spurning(x)
            if sp:
                points += 1
        print("Þú svaraðir",points,"af 10 spurningum réttum")
    
    if val == 2:
        valmynd= int(input("------Valmynd------\n1.Bæta við símaskrá\n2.Breyta símaskrá\n3.Eyða úr símaskrá\n4.Prenta símaskrá\n5.Hætta\nSláðu inn val: "))
        while valmynd != 5:
            if valmynd == 1:
                input_listi=[]
                input_listi.append(input("Sláðu inn nafn: "))
                input_listi.append(input("Sláðu inn kennitölu: "))
                input_listi.append(input("Sláðu inn símanúmer: "))
                skrifaIskra(input_listi,'simaskra.csv')
                
            if valmynd == 2:
                input_nafn=input("Sláðu inn nafn: ")
                input_gsm=input("Sláðu inn nýtt símanúmer: ")
                breytaUppl(lesaiSkra('simaskra.csv'),input_nafn,input_gsm)
                
            if valmynd == 3:
                eyda_nafni=input("sláðu inn nafn einstaklingsins sem þú vilt eyða: ")
                eyda(lesaiSkra('simaskra.csv'),eyda_nafni)
                
            if valmynd == 4:
                prenta(lesaiSkra('simaskra.csv'))

            valmynd= int(input("------Valmynd------\n1.Bæta við símaskrá\n2.Breyta símaskrá\n3.Eyða úr símaskrá\n4.Prenta símaskrá\n5.Hætta\nSláðu inn val: "))


    val = int(input("-----Valmynd-----\n1.Spurningabanki\n2.Símaskrá\nSláðu inn val: "))
