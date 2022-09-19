###----------EXO_1----------###

def mafonctioncool(x:int) -> int:
    """
    Cette fonction fait le calcul de x² + 2x + 10
    >>> mafonctioncool(4)
    34
    >>> mafonctioncool(5)
    45
    """
    

     
    assert type(x) == int, "Veuillez mettre un nombre entier."
    return x**2+2*x+10

#print(mafonctioncool(5))


###----------EXO_2----------###
def soustraction(x:int, y:int) -> int:
    """
    Cette fonction fais le calcul de x-y
    >>> soustraction(5,4)
    1
    >>> soustraction(8,4)
    4
    """
    
    assert type(x) == int and type(y) == int, 'Veuillez renter un nombre entier dans vos paramètres'
    
    
    return x-y


###----------EXO_3----------###
def multiplication(m:int, n:int) -> int:
    """
    Cette fonction fais le calcul de m*n
    >>> multiplication(5,4)
    20
    >>> multiplication(8,3)
    24
    """
    
    assert type(m) == int and type(n) == int, 'Veuillez renter un nombre entier dans vos paramètres'
    
    
    return m*n


###----------EXO_4----------###

def division(d:int, i:int) -> float:
    """
    Cette fonction fais le calcul de d/i
    >>> division(20,4)
    5.0
    >>> division(24,3)
    8.0
    """
    
    assert type(d) == int and type(i) == int, 'Veuillez renter un nombre entier dans vos paramètres'
    assert i !=0, 'Votre dénominateur ne doit pas être 0'
    
    
    return d/i

#print(division(50,5))

###----------EXO_5----------###

def volume_pave(longueur:int, largeur:int, profondeur:int) -> int:
    """
    Cette fonction fais le calcul du pavé
    >>> volume_pave(5,8,6)
    240
    >>> volume_pave(7,10,15)
    1050
    """
    
    assert type(longueur) == int and type(largeur) == int and type(profondeur) == int, 'Veuillez renter un nombre entier dans vos paramètres'
    
    
    return longueur * largeur * profondeur




if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)