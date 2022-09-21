a=0
b=-1
while b != 0:
    b = input("Vous allez additioner les nombre rentrés ici (faite 0 pour avoir le résultat) : ")
    b = int(b)
    a = a + b
print("La somme des valeurs que vous avez rentré est de : "+str(a))