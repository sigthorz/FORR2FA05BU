import random
vopnListi=["Sverð","Spjót","Exi"]
class Hermadur:
    def __init__(self,n):
        self.aettbalkur=n
        self.lif=random.randint(1,5)
        self.vopn=random.randint(0,2)
        self.afl=random.randint(1,5)
    def __str__(self):
        return "Ættbálkur: {} Líf: {} Vopn: {} Afl: {}".format(self.aettbalkur,self.lif,vopnListi[self.vopn],self.afl)
def aettbalkar(nafn,fjoldi):
    aettbalkur=[]
    for i in range(fjoldi):
        p= Hermadur(nafn)
        aettbalkur.append(p)
    return aettbalkur

