# Programme du Jeu de rôle / combat textuel - exercice Docstrings - Geoffroy Streit - apprentissage Python 
from random import randint
print("""⚔️  Jeu de rôle de combat textuel 🎲
      
Vous allez devoir combattre un redoutable adversaire.
Il est plus fort que vous, mais vous disposez de 3 potions de soins,
et vous avez l'initiative !
C'est un jeu au tour par tour. Attaques simples.
Vous disposez de 50 points de vie ainsi que votre adversaire.
Le tour ou vous choisirez de prendre une potion, 
vous n'attaquerez pas, mais votre adversaire, si !
A chaque attaque, dégats aléatoires : 
Vous : 5 à 10 points de Dégats. 
Adversaire : 5 à 15 !
Vos potions vous soigneront entre 15 et 50 point de vie.
Sortirez-vous vainqueur de cette confrontation ?!
Que le combat commence !""")

vies_joueur = 50
vies_ennemi = 50
potions = 3
actions = ['1', '2']

while True:
    print("⚔️ " * 30)
    choix=""
    while choix not in actions:
       choix = input("Souhaitez vous attaquer (1) ⚔️  ou prendre une potion (2) 🧪 ")

    if choix == '1':  # attaque
        degats_joueurs = randint(5, 10)
        degats_ennemi = randint(5, 15)
        vies_ennemi -= degats_joueurs
        print(f"⚔️  Vous avez infligé {degats_joueurs} points de dégats à l'ennemi 🗡️")
        if vies_ennemi < 1:
            print("Votre ennemi est mort ✌️  Vous avez gagné !! 🥁")
            break
        vies_joueur -= degats_ennemi
        print(f"⚔️  L'ennemi vous a infligé {degats_ennemi} points de dégats 🪓")
        if vies_joueur < 1:
            print("Vous êtes mort 🩻 GAME OVER !! 🙇")
            break         
        print(f"Il vous reste {vies_joueur} points de vie 💓")
        print(f"Il lui reste {vies_ennemi} points de vie 💟")
    else: # potion
        if potions:
            potions -= 1
            print("Il vous reste {potions} potions 🧪")
            vies_soignees = randint(15,50)
            vies_joueur += vies_soignees
            print(f"Vous récupérez 🧪 {vies_soignees} point de vie 💓")
            degats_ennemi = randint(5, 15)
            vies_joueur -= degats_ennemi
            print(f"⚔️ L'ennemi vous a infligé {degats_ennemi} points de dégats.🪓")
            print(f"Il vous reste {vies_joueur} points de vie 💓")
            print(f"Il lui reste {vies_ennemi} points de vie 💟")
        else:
            print("Vous n'avez plus de potions 🧪")

print("Fin du jeu")
