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
    b = 0
    a = random.randint(0,100)
    while b != a:
        b = input("Veuillez rentrer une valeur : ")
        b = int(b)
        if b < a:
            print("Votre nombre est supérieur au nombre choisit par le programme")
        else:
            print('Votre nombre est inférieur au nombre choisit par le programme')
    print("Vous avez trouvé le bon numéro qui est "+str(a))

###----------EXO_6----------###

def diviseur(nombre:int) -> None:
    """
    Cette fonction affiche les diviseurs du nombre en parametre
    >>> diviseur(36)
    1
    2
    3
    4
    6
    9
    12
    18
    36
    """
    # Loop over all factors
    for i in range(1, nombre + 1):
        if nombre % i == 0:
            print(i)


###----------EXO_7----------###


### Q1

def nombres_pairs(chiffre:int) -> None:
    """
    Cette fonction affiche les nombres pairs de 0 au nombre rentré en paramètre.
    >>> nombres_pairs(50)
    2
    4
    6
    8
    10
    12
    14
    16
    18
    20
    22
    24
    26
    28
    30
    32
    34
    36
    38
    40
    42
    44
    46
    48
    50
    """
    for i in range(1, chiffre + 1):
        if i % 2 == 0:
            print(i)


### Q2

def nombres_impairs(chiffre:int) -> None:
    """
    Cette fonction affiche les nombres pairs de 0 au nombre rentré en paramètre.
    >>> nombres_impairs(25)
    1
    3
    5
    7
    9
    11
    13
    15
    17
    19
    21
    23
    25
    """
    for i in range(1, chiffre + 1):
        if i % 2 != 0:
            print(i)



###----------EXO_8----------###


def additions_successives(chiffre:int) -> int:
    """
    Cette fonction donne le résultat d'additions successive des nombres rentrés par l'utilisateur.
    """
    a=0
    b=-1

    while b != 0:

        b = input("Vous allez additioner les nombre rentrés ici (faite 0 pour avoir le résultat) : ")
        b = int(b)
        a = a + b

    print("La somme des valeurs que vous avez rentré est de : "+str(a))


###----------EXO_9----------###

def nombre_occurence(chaine:str, x:str) -> int:
    """
    Cette fonction retourne le nombre de fois qu'une lettre x est présente dans un mot
    >>> nombre_occurence('banane', 'a')
    Le caractère a est présent 2 fois.
    >>> nombre_occurence('banane', 'n')
    Le caractère n est présent 2 fois.
    >>> nombre_occurence('anticonstitutionnellement', 't')
    Le caractère t est présent 5 fois.
    """
    a=0
    i = 0
    while i < len(chaine):
        if chaine[i] == x:
            a = int(a)
            a=a+1
            a = str(a)
        i=i+1
    print('Le caractère '+x+' est présent '+a+' fois.')
    



###----------EXO_10----------###

def est_palindrone(chaine:str):
    pass





###----------EXO_11----------###


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)