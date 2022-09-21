import random
b=0
a = random.randint(0,100)
while b != a:
    
    
    b = input("Veuillez rentrer une valeur : ")
    b = int(b)
    if b < a:
        print("Votre nombre est supérieur au nombre choisit par le programme")
    else:
        print('Votre nombre est inférieur au nombre choisit par le programme')
print("Vous avez trouvé le bon numéro qui est "+str(a))