from random import *

def randomListi(fjlisti, randbyrjun, randendir):
    listi_1=[]
    for x in range(fjlisti):
        listi_1.append(randint(randbyrjun,randendir))
    for x in range(len(listi_1)):
        if x == len(listi_1) - 1:
            print(listi_1[x])
        else:
            print(listi_1[x], end="-")
    print()
    halda_afram = True
    while halda_afram:
        halda_afram = False
        for x in listi_1:
            if x == 15:
                listi_1.remove(x)
                halda_afram = True
    print("Hérna er búið að eyða 15 úr listanum: ")
    print(*listi_1)
    print()
    for x in range(len(listi_1)):
        if listi_1[x] == 12:
            listi_1[x] = listi_1[x] + 10
    print("Hérna er búið að breyta öllum 12 í 22")
    print(listi_1,"\n")
    list_comp = [x+100 for x in listi_1]
    print("Hérna er búið að bæta 100 við allar tölurnar")
    print(list_comp)


def fjoldi_orda(setning):
    res = len(setning.split())
    lengd_set = str(res)
    return lengd_set

def skammstofun(setning):
    skamm_list = setning.split()
    s_s = ""
    for x in skamm_list:
        s_s = s_s + x[0].upper()
    return s_s

def print_dict(dictation_2):
    print("Nafn:\tLaun:")
    for i, x in dictation_2.items():
        print(i, "\t", x)

def eyda(diction_1, eyda_nafni):
    diction_1.pop(eyda_nafni)
    return diction_1


def dictionary():
    print("\nHérna ætlum við að skrá laun einstaklings, breyta og bæta þau.")
    print("Vinsamlegast Sláðu inn nafn og laun 5 einstaklinga.")
    diction_3 = {}
    samaNafn = True
    for x in range(5):
        samaNafn = True
        notkey = str(input("Sláðu inn nafn einstaklings: "))
        notvalue = int(input("Sláðu inn laun hans/hennar:"))
        while samaNafn:
            if notkey in diction_3.keys():
                notkey = str(input("Það Lýtur út fyrir að tveir af þeim sem þú skráðir inn höfðu sama nafn. Prófaðu að slá inn eftir nafn hans: "))
            else:
                diction_3[notkey] = notvalue
                samaNafn = False
    halda_afram_diction_3 = True
    while halda_afram_diction_3:
        print()
        print("1. Breyta launum")
        print("2. Bæta inn einstaklingi")
        print("3. Eyða einstaklingi")
        print("4. Prenta út hver hefur hæstu launin")
        print("5. Prenta út heildarlaun")
        print("6. Hætta")
        valmynd_diction_3 = int(input("Sláðu inn hvað þú vilt gera: "))
        print()

        if valmynd_diction_3 == 1:
            while samaNafn == False:
                samaNafn = False
                notkey = str(input("Sláðu inn nafn einstaklings: "))
                if notkey in diction_3.keys():
                    notvalue = int(input("Sláðu inn nýju laun hans/hennar:"))
                    diction_3[notkey] = notvalue
                    samaNafn = True
                else:
                    print("Þessi manneskja er ekki í kerfinu. Reyndu aftur")
            print_dict(diction_3)

        elif valmynd_diction_3 == 2:
            samaNafn = True
            notkey = str(input("Sláðu inn nafn einstaklings: "))
            notvalue = int(input("Sláðu inn laun hans/hennar:"))
            while samaNafn:
                if notkey in diction_3.keys():
                    notkey = str(input("Þú slóst inn tvo einstaklinga sem heita það sama. Vinsamlegast sláðu inn eftirnafn þeirra: "))
                else:
                    diction_3[notkey] = notvalue
                    samaNafn = False

        elif valmynd_diction_3 == 3:
            eydanafn = str(input("Sláðu inn nafn einstaklingsins sem þú vilt eyða úr kerfinu: "))
            diction_3 =  eyda(diction_3, eydanafn)
            print_dict(diction_3)
        
        elif valmynd_diction_3 == 4:
            listidiction_3 = []
            for x, i in diction_3.items():
                listidiction_3.append(i)
                if max(listidiction_3) == diction_3[x]:
                    haestulaunnafn = x
            print("Sá sem fær mest borgað er", haestulaunnafn + ", hann fær ", max(listidiction_3),"kr")
        
        elif valmynd_diction_3 == 5:
            heildarlaun = 0
            for s in diction_3.values():
                heildarlaun += s
            print("Heildarlaun allra eru:", heildarlaun)

        elif valmynd_diction_3 == 6:
            halda_afram_diction_3 = False
        
        else:
            print("Rangt inn slegið, reyndur aftur.")
                    
            


    

halda_afram = True

while halda_afram:
    print()
    print("---Valmynd---\n1. Listi \n2. Strengur \n3. Dictionary \n4. Spurningar \n5. Hætta")
    valmynd = int(input("\nSláðu inn númer liðsins sem þig langar að framkvæma: "))

    if valmynd == 1:
        print()
        randomListi(20, 10, 20)
    elif valmynd == 2:
        print()
        print("Sláðu inn texta")
        textil2 = str(input())
        print()
        print("Fjöldi orða sem er í þessum texta er:", fjoldi_orda(textil2))
        print("Skammstöfun allra orðanna er:", skammstofun(textil2))
    elif valmynd == 3:
        dictionary()
    elif valmynd == 4:
        print("1. Hvenær er eðilegra að nota tuple heldur en lista í forritun og hvers vegna?")
        print("1 svar: Eina skiptið sem ég myndi nota tuple í stað lista eða þegar ég er að geyma eitthvað sem mun aldrei breytast")
        print("t.d. ef út af eitthverjari ástæðu þarftu að geyma stafróið í kóðanum þínum því það mun aldrei breytast.")
        print("1a. Hverjir eru kostir og gallar Tuple?")
        print("1a svar: Það er gott að geyma hluti í Tuple en þeir festast og það er ekki hægt að breyta tuple svo ég persónulega myndi aldrei nota það.")
        print("1b. Hverjir eru kostir og gallar tuple?")
        print("1b svar: Það góða við að nota lista er að þú getur geymt mikið þarna inni og það er hægt að breyta því eins mikið og þú vilt")
        print("2. Hvernig er einföld útskýring á hvað fall er?")
        print("2 svar: fall er þegar þú setur inn t.d. eitthverjar tölur og færð útkomum frá því. Einfaldasta og stys_sta leiðin til að útskýra er input og output.")
        print("2a. Hvað einkennir vel gert fall?")
        print("2a svar: Í fyrsta lagi að það virkar og líka að það er tekur inn t.d. variables og endurnefnir þær svo það er hægt að nota fallið aftur og aftur með mismunandi variables.")
    elif valmynd == 5:
        halda_afram = False
    else:
        print("Rangt slegið inn")