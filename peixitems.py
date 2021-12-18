from pickle import*
def remplire():
    fp = open("prix.dat","wb")
    n = int(input("Donner n : "))
    while n < 2 :
        n = int(input("Donner n : "))
    for i in range(n):
        d = {}
        d["item"] = input("Item : ")
        d["prix"] = float(input("prix : "))
        while d["prix"] < 0:
            d["prix"] = float(input("prix > 0: "))
        dump(d,fp)
    return n
def affiche(n):
    fp = open("prix.dat","rb")
    for i in range(n):
        d = load(fp)
        print(d["item"],d["prix"])
n = remplire()
affiche(n)
