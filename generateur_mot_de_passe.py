# Programme Générateur de Mots de Passe - exercice Chaînes et Random - Apprentissage Python
import random
import string

print("""
╔═══════════════════════════════════════╗
║  🔐 GÉNÉRATEUR DE MOTS DE PASSE 🔐   ║
╔═══════════════════════════════════════╝
Crée un mot de passe sécurisé aléatoire !
""")

# Demander la longueur du mot de passe
while True:
    longueur_input = input("Longueur du mot de passe (8-32) : ")
    
    if longueur_input.isdigit():
        LONGUEUR = int(longueur_input)
        if 8 <= LONGUEUR <= 32:
            break
        else:
            print("⚠️  La longueur doit être entre 8 et 32 caractères !")
    else:
        print("⚠️  Entre un nombre valide !")

# Demander les options
print("\n--- Options du mot de passe ---")

majuscules_input = input("Inclure des majuscules (A-Z) ? (o/n) : ").lower()
INCLURE_MAJUSCULES = majuscules_input == "o"

minuscules_input = input("Inclure des minuscules (a-z) ? (o/n) : ").lower()
INCLURE_MINUSCULES = minuscules_input == "o"

chiffres_input = input("Inclure des chiffres (0-9) ? (o/n) : ").lower()
INCLURE_CHIFFRES = chiffres_input == "o"

symboles_input = input("Inclure des symboles (!@#$%...) ? (o/n) : ").lower()
INCLURE_SYMBOLES = symboles_input == "o"

# Vérifier qu'au moins une option est sélectionnée
if not (INCLURE_MAJUSCULES or INCLURE_MINUSCULES or INCLURE_CHIFFRES or INCLURE_SYMBOLES):
    print("\n⚠️  Tu dois sélectionner au moins une option !")
    print("Génération d'un mot de passe avec toutes les options par défaut...")
    INCLURE_MAJUSCULES = True
    INCLURE_MINUSCULES = True
    INCLURE_CHIFFRES = True
    INCLURE_SYMBOLES = True

# Construire la liste des caractères possibles
caracteres_possibles = ""

if INCLURE_MAJUSCULES:
    caracteres_possibles += string.ascii_uppercase
if INCLURE_MINUSCULES:
    caracteres_possibles += string.ascii_lowercase
if INCLURE_CHIFFRES:
    caracteres_possibles += string.digits
if INCLURE_SYMBOLES:
    caracteres_possibles += "!@#$%^&*()_+-=[]{}|;:,.<>?"

# Générer le mot de passe
mot_de_passe = ""
for i in range(LONGUEUR):
    caractere_aleatoire = random.choice(caracteres_possibles)
    mot_de_passe += caractere_aleatoire

# Afficher le résultat
print("\n" + "="*50)
print(f"🎉 Ton mot de passe généré : {mot_de_passe}")
print("="*50)
print(f"\nLongueur : {len(mot_de_passe)} caractères")
print("💡 Conseil : note-le dans un endroit sûr !")
