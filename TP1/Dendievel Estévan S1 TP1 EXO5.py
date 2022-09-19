base = input("Quelle est la taille de la base du triangle : ")
hauteur = input("Quelle est la taille de la hauteur du triangle : ")

base=int(base)
hauteur=int(hauteur)

aire = base*hauteur

base=str(base)
hauteur=str(hauteur)
aire=str(aire)

print("\nTaille de la base    : "+base+" cm.\nTaille de la hauteur : "+hauteur+" cm.\nAire du triangle     : "+aire+" cm².")