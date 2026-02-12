# Programme Calculatrice Simple - exercice Conditions et Boucles - Apprentissage Python
import sys

print("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   🧮 CALCULATRICE SIMPLE 🧮
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Effectue des opérations mathématiques de base !
""")

while True:
    print("\n--- Menu des opérations ---")
    print("1. Addition (+)")
    print("2. Soustraction (-)")
    print("3. Multiplication (×)")
    print("4. Division (÷)")
    print("5. Quitter")
    
    choix = input("\nChoisis une opération (1-5) : ")
    
    if choix == "5":
        print("\n👋 Merci d'avoir utilisé la calculatrice !")
        print("À bientôt !")
        sys.exit()
    
    if choix not in ["1", "2", "3", "4"]:
        print("⚠️  Erreur : choisis un nombre entre 1 et 5 !")
        continue
    
    # Demander les deux nombres
    nombre1 = input("Entre le premier nombre : ")
    nombre2 = input("Entre le deuxième nombre : ")
    
    # Vérifier que ce sont bien des nombres
    try:
        num1 = float(nombre1)
        num2 = float(nombre2)
    except ValueError:
        print("⚠️  Erreur : ce ne sont pas des nombres valides !")
        continue
    
    # Effectuer le calcul selon le choix
    if choix == "1":
        resultat = num1 + num2
        operation = "+"
        print(f"\n✅ Résultat : {num1} {operation} {num2} = {resultat}")
    elif choix == "2":
        resultat = num1 - num2
        operation = "-"
        print(f"\n✅ Résultat : {num1} {operation} {num2} = {resultat}")
    elif choix == "3":
        resultat = num1 * num2
        operation = "×"
        print(f"\n✅ Résultat : {num1} {operation} {num2} = {resultat}")
    elif choix == "4":
        if num2 == 0:
            print("⚠️  Erreur : division par zéro impossible !")
        else:
            resultat = num1 / num2
            operation = "÷"
            print(f"\n✅ Résultat : {num1} {operation} {num2} = {resultat:.2f}")
