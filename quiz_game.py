import random

# Quiz questions about Ghana
questions = [
    {
        "question": "What is the capital city of Ghana?",
        "options": ["A. Kumasi", "B. Accra", "C. Tamale", "D. Sekondi-Takoradi"],
        "answer": "B"
    },
    {
        "question": "Which year did Ghana gain independence?",
        "options": ["A. 1945", "B. 1957", "C. 1960", "D. 1966"],
        "answer": "B"
    },
    {
        "question": "Who was Ghana's first president?",
        "options": ["A.Jerry Rawlings", "B. Kwame Nkrumah", "C. John Kufuor", "D. Nana Akufo-Addo"],
        "answer": "B"
    },
    {
        "question": "What is the currency of Ghana?",
        "options": ["A. Cedi", "B. Naira", "C. Dollar", "D. Euro"],
        "answer": "A"
    },
    {
        "question": "Which of these is a famous Ghanaian dish?",
        "options": ["A. Fufu", "B. Jollof Rice", "C. Banku", "D. All of the above"],
        "answer": "D"
    },
    {
        "question": "What is the name of Ghana's largest artificial lake?",
        "options": ["A. Lake Bosomtwe", "B. Lake Volta", "C. Lake Tanganyika", "D. Lake Malawi"],
        "answer": "B"
    },
    {
        "question": "Which European country first arrived in Ghana?",
        "options": ["A. British", "B. French", "C. Portuguese", "D. Dutch"],
        "answer": "C"
    },
    {
        "question": "What is Ghana's most exported mineral resource?",
        "options": ["A. Diamond", "B. Bauxite", "C. Gold", "D. Manganese"],
        "answer": "C"
    },
    {
        "question": "Which of these is a traditional Ghanaian fabric?",
        "options": ["A. Kente", "B. Ankara", "C. Batik", "D. All of the above"],
        "answer": "A"
    },
    {
        "question": "What is the name of Ghana's parliament building?",
        "options": ["A. The Golden Tower", "B. Job 600",
                    "C. The State Hall", "D. Parliament House"],
        "answer": "D"
    },
    {
        "question": "Which region in Ghana is known for its gold mines?",
        "options": ["A. Ashanti Region", "B. Northern Region",
                    "C. Volta Region", "D. Central Region"],
        "answer": "A"
    },
    {
        "question": "What is the most widely spoken indigenous language in Ghana?",
        "options": ["A. Ewe", "B. Ga", "C. Twi", "D. Dagbani"],
        "answer": "C"
    },
    {
        "question": "Which festival is celebrated by the Ashanti people?",
        "options": ["A. Homowo", "B. Hogbetsotso", "C. Akwasidae", "D. Aboakyir"],
        "answer": "C"
    },
    {
        "question": "What is the name of Ghana's highest mountain?",
        "options": ["A. Mount Afadjato", "B. Mount Kilimanjaro",
                    "C. Mount Everest", "D. Mount Atiwa"],
        "answer": "A"
    },
    {
        "question": "Which famous slave trade castle is located in Ghana?",
        "options": ["A. Elmina Castle", "B. Cape Coast Castle",
                    "C. Christiansborg Castle", "D. All of the above"],
        "answer": "D"
    }
]

# Global variables
leaderboard = []
used_questions = []

def display_welcome():
    print("\nWelcome to the Ghana Quiz Game!")
    print("Test your knowledge about Ghana with 5 random questions.")
    print("Each correct answer gives you 1 point.\n")

def select_questions():
    available_questions = [q for q in questions if q not in used_questions]
    if len(available_questions) < 5:
        print("\nResetting question pool to allow repetition.\n")
        used_questions.clear()
        available_questions = questions.copy()
    selected_questions = random.sample(available_questions, 5)
    used_questions.extend(selected_questions)
    return selected_questions

def run_quiz():
    score = 0
    quiz_questions = select_questions()
    for i, q in enumerate(quiz_questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q['options']:
            print(option)
        while True:
            user_answer = input("Your answer (A/B/C/D): ").upper()
            if user_answer in ['A', 'B', 'C', 'D']:
               if user_answer == q['answer']:
                  print("Correct!")
                  score += 1
               else:
                  print(f"Wrong! The correct answer is {q['answer']}.")
               break
            else:
                print("Invalid input. Please enter A,B,C, or D")
    print(f"\nYour final score: {score}/5")
    return score

def update_leaderboard(score):
    while True:
        name = input("Enter your name: ").strip()
        player_exists = next((item for item in leaderboard if item["name"].lower() == name.lower()), None)
        if player_exists:
            while True:
                choice = input(f"A player named '{name}' already exists. Do you want to update your score? (yes/no): ").lower()
                if choice == 'yes':
                    player_exists['score'] = score
                    print(f"Score for {name} has been updated.")
                    break
                elif choice == 'no':
                    print("Please enter a different name.")
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
            if choice == 'yes':
                break
        else:
            leaderboard.append({"name": name, "score": score})
            print(f"Welcome, {name}!")
            break

    leaderboard.sort(key=lambda x: x['score'], reverse=True)

def display_leaderboard():
    print("\nLEADERBOARD")
    print("-----------")
    if not leaderboard:
        print("No scores yet!")
    else:
        for i, entry in enumerate(leaderboard, 1):
            print(f"{i}. {entry['name']}: {entry['score']}/5")

def main():
    while True:
        display_welcome()
        score = run_quiz()
        update_leaderboard(score)
        display_leaderboard()
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing! Medaase!")
            break

if __name__ == "__main__":
    main()