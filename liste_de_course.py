# Programme de liste de courses - exercice Docstrings - Geoffroy Streit - apprentissage Python 
import sys

c="" # choix utilisateur
liste=[]  # liste de course

while True:  # not c=='5':
    # Menu 5 options
    print("1: Ajouter un élément à la liste")
    print("2: Retirer un élément à la liste")
    print("3: Afficher la liste")
    print("4: Vider la liste")
    print("5: Quitter")
    c = input("☛ Votre choix : ")

    #test entree et branche bloc instructions adéquates 

    if c=='1':  #ajout
        element = input("Entrez le nom de l'élément à ajouter à la liste de course : ") 
        if element != "":
            liste.append(element)
            print(f"L'élément {element} a bien été ajouté à la liste.")
        else:
            print("Vous n'avez fait aucune entrée.")

    elif c=='2':  #retrait
        element = input("Entrez le nom d'un élément à retirer de la liste de course : ")
        if element in liste:
            liste.remove(element)
            print(f"L'élément {element} a bien été supprimé de la liste.")
        else:
            print(f"L'élément {element} n'est pas dans liste.")

    elif c=='3':  #affiche
        print("Voici le contenu de votre liste :")
        if liste:
            for p, element in enumerate(liste):
                print(f"{p}. {element}")
        else:
            print("Votre liste ne contient aucun élément.")

    elif c=='4':  #vide
        liste.clear()
        print("La liste a été vidée de son contenu.")

    elif c=='5':  #sort
        print("À bientot !")
        sys.exit()

    else:  # mauvaise saisie
        print("Veuillez entrer un chiffre de 1 à 5.")

    print("―"*50)


# fin de programme