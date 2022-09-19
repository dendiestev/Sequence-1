###----------EXO_1----------###

### Q1

def parcourir_for(mot:str) -> None:
    """
    Ensemble des caractères du mot
    >>> parcourir_for('lukaku')
    l
    u
    k
    a
    k
    u
    """
    for s in mot:
        print(s)

### Q2

def parcourir_tantque(mot:str) -> None:
    """
    Ensemble des caractères du mot
    >>> parcourir_tantque('lopotichat')
    l
    o
    p
    o
    t
    i
    c
    h
    a
    t
    """
    i = 0
    while i < len(mot):
        print(mot[i])
        i=i+1

###----------EXO_2----------###

def table_multiplication(table:int) -> None:
    """
    Donne la table de multiplication du parametre table
    >>> table_multiplication(5)
    0
    5
    10
    15
    20
    25
    30
    35
    40
    45
    50
    """
    assert table > 0 , 'Le nombre doit être positif'
    i = 0
    while i < 11:
        print(table*i)
        i=i+1


###----------EXO_3----------###

def somme(chiffre:int) -> int:

    """
    Cette fonction donne la somme des entier de 1 à la var chiffre.
    >>> somme(5)
    15
    """

    a=0
    i=0
    while i <= chiffre:
        a=a+i
        i=i+1
    print(a)

###----------EXO_4----------###

def factorielle(a:int) -> int:
    """
    Cette fonction donne la factorielle d'un nombre.
    >>> factorielle(10)
    3628800
    >>> factorielle(2)
    2
    >>> factorielle(5)
    120
    """
    F = 1
    for k in range(2,a+1):
        F = F * k
    print(F)

###----------EXO_5----------###
import random
def juste_prix() -> None:
    a = random.randint(0,100)
    b = input("Veuillez rentrer une valeur")
    while b != a:
        
        if b > a:
            print("Votre nombre est supérieur au nombre choisit par le programme")
        else:
            print('Votre nombre est inférieur au nombre choisit par le programme')

###----------EXO_6----------###

def diviseur(nombre:int) -> None:
    """
    Cette fonction affiche les diviseurs du nombre en parametre
    """
    # Loop over all factors
    for i in range(1, nombre + 1):
        if nombre % i == 0:
            pass


###----------EXO_7----------###






if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)