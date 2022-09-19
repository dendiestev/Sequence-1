def categories(age:int):
    
    """
    Cette fonction permet de classer les catégories des enfants au foot
    >>> categories(6)
    'Débutants'
    >>> categories(16)
    'Cadets'
    >>> categories(8)
    'Poussins'
    """
    age = input("Veuillez nous préciser l'âge de votre enfant : ")
    assert type(age) == int , 'Veuillez renter un nombre entier dans vos paramètres'
    
    
    if age >= 5 and age <= 6 :
        return 'Débutants'
    if age >= 7 and age <= 8 :
        return 'Poussins'
    if age >= 9 and age <= 10 :
        return 'Benjamins'
    if age >= 11 and age <= 12:
        return 'Pupilles'
    if age >= 13 and age <= 14:
        return 'Minimes'
    if age >= 15 and age <= 16:
        return 'Cadets'
    if age >= 17 and age <= 18:
        return 'Juniors'
    
    
    

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)