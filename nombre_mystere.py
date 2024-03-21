# Programme du Jeu du Nombre mystère - exercice Docstrings - Geoffroy Streit - apprentissage Python 
import sys
from random import randint
print("""
¯\_(ツ)_/¯ Jeu du Nombre mystère ¯\_(ツ)_/¯
Tu dois deviner un nombre mystère entre 0 et 100 !
Procéde par tatonnement, tu auras le droit à 5 essais.
""")
NOMBRE_MYSTERE = randint(0, 100)
NOMBRE_JOUEUR = 101
ESSAI = 5

while ESSAI > 0:
    print(f"Il te reste {ESSAI} essai{'s' if ESSAI > 1 else ''}.")
    n = input("Devine le nombre : ")
    if n.isdigit():
        NOMBRE_JOUEUR = int(n)

        if 0 < NOMBRE_JOUEUR <= 100:
            if NOMBRE_JOUEUR > NOMBRE_MYSTERE:
                print(f"Le nombre mystère est plus petit que {NOMBRE_JOUEUR}.")
            elif NOMBRE_JOUEUR < NOMBRE_MYSTERE:
                print(f"Le nombre mystère est plus grand que {NOMBRE_JOUEUR}.")            
            else:
                print(F"Bravo ! Le nombre mystère était bien {NOMBRE_MYSTERE}.")
                print(f"Tu as trouvé le nombre en {1+5-ESSAI} essai{'s' if ESSAI > 1 else ''}.")
                print("Fin du jeu")
                sys.exit()
            ESSAI -= 1
        else:
                print("Un nombre de 0 à 100 inclus...")
    else:
        print("Ce n'est pas un nombre...")
print(f"Dommage, le nombre mystère était {NOMBRE_MYSTERE}.")
print("Fin du jeu")
sys.exit()