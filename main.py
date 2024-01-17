import masik

szoveg:str="Első szöveg" #globális változó ebben a modulban látszik

print(szoveg)

#print(szoveg2) #ez a változó itt nem látszik

def eljaras():
    szoveg:str="Másik szöveg az eljárásban"
    print(szoveg)
    szoveg2:str="eljarásban"
    print(szoveg2) #lokális változó, csak az eljárásban érhető el

#eljaras()

print(szoveg)
#print(szoveg2)

def masik_eljaras():
    #egyszerü adatípus mint string
    print(masikvalami) #NameError: name 'masikvalami' is not defined
    print(valami)  # ismeri a változott csak nem tudja hogy mi az érték,mert azt csak késöbb adtuk meg neki
    valami: str = "valami"

#masik_eljaras()

def elj2(valt:int):
    valt+=1
    print(valt) #13

valt=12

elj2(valt)

print("valt",valt) #valt 12

def elj3(lista):
    #összetett adatípus, lista
    lista[0]=1111111
    for i in range(0,len(lista),1):
        print(lista[i])

lista=[1,2,3,4,5,6,7]

elj3(lista)

for i in range(0,len(lista),1):
    print("lista az eljárás hívása utén",lista[i])