# Programme Gestionnaire de Tâches - exercice Listes et Manipulation - Apprentissage Python
import sys
from datetime import datetime

print("""
╔═══════════════════════════════╗
║   GESTIONNAIRE DE TÂCHES      ║
╚═══════════════════════════════╝
Organise tes tâches quotidiennes facilement !
""")

# Liste pour stocker les tâches
liste_taches = []

def afficher_taches():
    """Affiche toutes les tâches avec leur statut"""
    if len(liste_taches) == 0:
        print("\n Aucune tâche pour le moment. Ta liste est vide !")
    else:
        print(f"\n Tu as {len(liste_taches)} tâche{'s' if len(liste_taches) > 1 else ''} :")
        print("-" * 50)
        for index, tache in enumerate(liste_taches, 1):
            statut = "✓" if tache["terminee"] else "○"
            print(f"{index}. [{statut}] {tache['nom']}")
        print("-" * 50)

def ajouter_tache():
    """Ajoute une nouvelle tâche à la liste"""
    nom_tache = input("\n+ Nom de la tâche : ").strip()
    if nom_tache:
        nouvelle_tache = {
            "nom": nom_tache,
            "terminee": False,
            "date_creation": datetime.now().strftime("%d/%m/%Y %H:%M")
        }
        liste_taches.append(nouvelle_tache)
        print(f" Tâche '{nom_tache}' ajoutée avec succès !")
    else:
        print("  Le nom de la tâche ne peut pas être vide !")

def marquer_terminee():
    """Marque une tâche comme terminée"""
    if len(liste_taches) == 0:
        print("\n  Aucune tâche à marquer comme terminée !")
        return
    
    afficher_taches()
    numero = input("\nNuméro de la tâche à marquer comme terminée : ")
    
    if numero.isdigit():
        index = int(numero) - 1
        if 0 <= index < len(liste_taches):
            if liste_taches[index]["terminee"]:
                print(f"\n La tâche '{liste_taches[index]['nom']}' est déjà terminée !")
            else:
                liste_taches[index]["terminee"] = True
                print(f"\n Tâche '{liste_taches[index]['nom']}' marquée comme terminée !")
        else:
            print("\n  Numéro de tâche invalide !")
    else:
        print("\n  Entre un nombre valide !")

def supprimer_tache():
    """Supprime une tâche de la liste"""
    if len(liste_taches) == 0:
        print("\n  Aucune tâche à supprimer !")
        return
    
    afficher_taches()
    numero = input("\nNuméro de la tâche à supprimer : ")
    
    if numero.isdigit():
        index = int(numero) - 1
        if 0 <= index < len(liste_taches):
            tache_supprimee = liste_taches.pop(index)
            print(f"\n  Tâche '{tache_supprimee['nom']}' supprimée !")
        else:
            print("\n  Numéro de tâche invalide !")
    else:
        print("\n  Entre un nombre valide !")

def afficher_statistiques():
    """Affiche les statistiques des tâches"""
    if len(liste_taches) == 0:
        print("\n Aucune statistique à afficher.")
        return
    
    taches_terminees = sum(1 for tache in liste_taches if tache["terminee"])
    taches_en_cours = len(liste_taches) - taches_terminees
    pourcentage = (taches_terminees / len(liste_taches)) * 100
    
    print("\n" + "="*50)
    print("STATISTIQUES")
    print("="*50)
    print(f"Total de tâches : {len(liste_taches)}")
    print(f"Tâches terminées : {taches_terminees}")
    print(f"Tâches en cours : {taches_en_cours}")
    print(f"Progression : {pourcentage:.1f}%")
    print("="*50)

# Boucle principale du programme
while True:
    print("\n┌─── MENU PRINCIPAL ───┐")
    print("│ 1. Voir les tâches   │")
    print("│ 2. Ajouter une tâche │")
    print("│ 3. Marquer terminée  │")
    print("│ 4. Supprimer tâche   │")
    print("│ 5. Statistiques      │")
    print("│ 6. Quitter           │")
    print("└──────────────────────┘")
    
    choix = input("\nTon choix (1-6) : ")
    
    if choix == "1":
        afficher_taches()
    elif choix == "2":
        ajouter_tache()
    elif choix == "3":
        marquer_terminee()
    elif choix == "4":
        supprimer_tache()
    elif choix == "5":
        afficher_statistiques()
    elif choix == "6":
        print("\n Au revoir ! À bientôt !")
        print("Bon courage avec tes tâches ! ")
        sys.exit()
    else:
        print("\n  Choix invalide ! Entre un nombre entre 1 et 6.")
