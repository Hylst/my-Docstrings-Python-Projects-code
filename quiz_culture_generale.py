# Programme Quiz de Culture Générale - exercice Listes et Dictionnaires - Apprentissage Python
import random

print("""
┌────────────────────────────┐
│  QUIZ DE CULTURE GÉNÉRALE  │
└────────────────────────────┘
Réponds correctement à un maximum de questions !
""")

# Banque de questions (liste de dictionnaires)
QUESTIONS = [
    {
        "question": "Quelle est la capitale de la France ?",
        "reponses": ["1. Lyon", "2. Paris", "3. Marseille", "4. Toulouse"],
        "correcte": 2
    },
    {
        "question": "Combien de continents y a-t-il sur Terre ?",
        "reponses": ["1. 5", "2. 6", "3. 7", "4. 8"],
        "correcte": 3
    },
    {
        "question": "Qui a peint la Joconde ?",
        "reponses": ["1. Van Gogh", "2. Picasso", "3. Michel-Ange", "4. Léonard de Vinci"],
        "correcte": 4
    },
    {
        "question": "Quel est le plus grand océan du monde ?",
        "reponses": ["1. Atlantique", "2. Indien", "3. Pacifique", "4. Arctique"],
        "correcte": 3
    },
    {
        "question": "En quelle année l'homme a-t-il marché sur la Lune ?",
        "reponses": ["1. 1965", "2. 1969", "3. 1972", "4. 1981"],
        "correcte": 2
    },
    {
        "question": "Combien de joueurs y a-t-il dans une équipe de football ?",
        "reponses": ["1. 9", "2. 10", "3. 11", "4. 12"],
        "correcte": 3
    },
    {
        "question": "Quelle est la planète la plus proche du Soleil ?",
        "reponses": ["1. Vénus", "2. Mercure", "3. Mars", "4. Terre"],
        "correcte": 2
    },
    {
        "question": "Combien de côtés a un hexagone ?",
        "reponses": ["1. 5", "2. 6", "3. 7", "4. 8"],
        "correcte": 2
    }
]

# Mélanger les questions
random.shuffle(QUESTIONS)

# Variables de score
score = 0
total_questions = len(QUESTIONS)

# Boucle du quiz
for index, question_data in enumerate(QUESTIONS, 1):
    print(f"\n━━━ Question {index}/{total_questions} ━━━")
    print(question_data["question"])
    print()
    
    for reponse in question_data["reponses"]:
        print(reponse)
    
    # Demander la réponse
    while True:
        choix = input("\nTa réponse (1-4) : ")
        if choix in ["1", "2", "3", "4"]:
            choix_int = int(choix)
            break
        else:
            print("⚠️  Entre un nombre entre 1 et 4 !")
    
    # Vérifier la réponse
    if choix_int == question_data["correcte"]:
        print("✅ Correct ! Bravo !")
        score += 1
    else:
        reponse_correcte = question_data["correcte"]
        print(f"❌ Faux ! La bonne réponse était : {question_data['reponses'][reponse_correcte-1]}")

# Afficher le score final
print("\n" + "="*50)
print("🏆 RÉSULTATS DU QUIZ 🏆")
print("="*50)
print(f"Score final : {score}/{total_questions}")

# Commentaire selon le score
pourcentage = (score / total_questions) * 100

if pourcentage == 100:
    commentaire = "🌟 Parfait ! Tu es un expert !"
elif pourcentage >= 75:
    commentaire = "👍 Très bien ! Belle performance !"
elif pourcentage >= 50:
    commentaire = "😊 Pas mal ! Continue comme ça !"
elif pourcentage >= 25:
    commentaire = "🤔 Tu peux faire mieux !"
else:
    commentaire = "💪 Révise et réessaie !"

print(f"({pourcentage:.0f}%) - {commentaire}")
print("\nMerci d'avoir joué ! 🎮")
