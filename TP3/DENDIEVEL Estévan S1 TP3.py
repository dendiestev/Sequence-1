###----------EXO_1----------###
def plus_grand(x:int, y:int) -> int :
    
    """
    Cette fonction donne la plus grande des 2 valeurs
    >>> plus_grand(4,9)
    9
    >>> plus_grand(7,2)
    7
    """
    
    if x > y :
        return x
    else :
        return y


###----------EXO_2----------###

def positif_negatif_nul(nombre:int) :
    
    """
    Cette fonction dit si un nombre est positif, négatif ou nul.
    >>> positif_negatif_nul(5)
    'Positif'
    >>> positif_negatif_nul(-9)
    'Négatif'
    >>> positif_negatif_nul(0)
    'Nul'
    """

    
    if nombre > 0:
        return 'Positif'
    elif nombre < 0:
        return 'Négatif'
    else:
        return 'Nul'


###----------EXO_3----------###
def entre_0_100(x:int):
    """
    Cette fonction dit si un nombre est compris enter 0 et 100
    >>> entre_0_100(5)
    True
    >>> entre_0_100(-101)
    False
    >>> entre_0_100(0)
    True
    """
    
    if x >= 0 and x <=100:
        return True
    else:
        return False


###----------EXO_4----------###
def est_pair(x:int):
    """Cette fonction dit si un nombre est pair ou non
    >>> est_pair(666)
    True
    >>> est_pair(999)
    False
    """
    if (x%2) == 0:
        return True
    else:
        return False


###----------EXO_5----------###
def calcul(a:int, b:int, signe:str) -> int:
    """
    Cette fonction donne le résultat en fonction du signe.
    >>> calcul(5,8,'+')
    13
    >>> calcul(10,5,'/')
    2.0
    """

    if signe == '+':
        return a+b
    if signe == '-':
        return a-b
    if signe == '*':
        return a*b
    if signe == '/':
        return a/b


###----------EXO_6----------###
def securite_password(mdp:str):
    """
    Cette fonction permet de vérifier la sécurité d'un mdp
    >>> securite_password('klhdsgbjdgbnjdobnwmlbnmwjbhn')
    'Mot de passe correct'
    >>> securite_password('kvh')
    'Mot de passe insuffisant'
    >>> securite_password('jflkkik')
    'Mot de passe toléré'
    """
    if len(mdp) >= 1 and len(mdp) <= 5:
        return 'Mot de passe insuffisant'
    if len(mdp) >= 6 and len(mdp) <=10:
        return 'Mot de passe toléré'
    if len(mdp) >= 11:
        return 'Mot de passe correct'



###----------EXO_7----------###
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

    # Mit en commentaire car fait planter les tests #
    # 
    # age = input("Veuillez nous préciser l'âge de votre enfant : ")

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





###----------EXO_8----------###

def prix(places:int, abonne:bool):

    """
    Cette fonction donne le prix à payer selon le nombre de places de cinéma que l'on achète.
    >>> prix(45, True)
    189.7
    >>> prix(3, False)
    18
    >>> prix(7, True)
    44.7
    """

    # Mit en commentaire car fait planter les tests #
    # 
    # places = input('Veuillez rentrer le nombre de places que vous souhaitez acheter.')

    assert type(places) == int , "Vous n'avez pas rentré un entier"
    
    if abonne:
        reduc = 10
        pourcent = 30/100
    else:
        reduc = 0
        pourcent = 0

    if places >= 3 and places <= 5:
        return (6*places+reduc)-pourcent
    if places >= 6 and places <= 15:
        return (5*places+reduc)-pourcent
    if places > 15:
        return (4*places+reduc)-pourcent





if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)