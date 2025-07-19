import random
import os

def get_questions():
    question_bank = {
        "name": "What's your name?",
        "age": "How old are you?",
        "color": "What's your favorite color?",
        "food": "What's your favorite food?",
        "city": "Which city do you live in?",
        "shs": "Which SHS did you attend?",
        "team": "What's your favourite soccer team?",
        "hobby": "What's a hobby you enjoy?",
        "dream": "What's your dream job?"
    }
    # Randomly select 5–7 unique questions each round
    selected_keys = random.sample(list(question_bank.keys()), k=random.randint(5, 7))
    return [(key, question_bank[key]) for key in selected_keys]

def collect_info():
    responses = {}
    questions = get_questions()
    for key, question in questions:
        responses[key] = input(f"{question} ")
    return responses

def generate_summary(data):
    summary = f"\nHello, {data.get('name', 'Friend')}!"
    if 'age' in data:
        summary += f" You are {data['age']} years old,"
    if 'color' in data:
        summary += f" love the color {data['color']},"
    if 'food' in data:
        summary += f" and enjoy eating {data['food']}."
    if 'city' in data:
        summary += f" Life must be awesome in {data['city']}!"
    if 'shs' in data:
        summary += f"\nYou attended {data['shs']} SHS — memories, right?"
    if 'team' in data:
        summary += f"\nSupporting {data['team']} must be a thrill!"
    if 'hobby' in data:
        summary += f"\nIn your free time, you love {data['hobby']}."
    if 'dream' in data:
        summary += f"\nAnd dreaming of becoming a {data['dream']}? Go for it!"
    return summary

def save_to_file(name, summary, rating):
    filename = f"{name}.txt"
    with open(filename, "w") as file:
        file.write(summary)
        file.write(f"\n\nUser Rating: {rating} stars\n")
    print(f"\n✅ Summary saved to '{filename}'.")

def assistant():
    while True:
        info = collect_info()
        summary = generate_summary(info)
        print("\n--- YOUR PERSONAL SUMMARY ---")
        print(summary)

        save = input("\nWould you like to save this summary to a file? (yes/no): ").lower()
        if save.startswith("y"):
            rating = input("How would you rate your assistant? (1 to 5 stars): ")
            save_to_file(info.get("name", "user"), summary, rating)

        again = input("\nWould you like to restart the process? (yes/no): ").lower()
        if not again.startswith("y"):
            print("\n👋 Thanks for chatting with your personal assistant!")
            break

assistant()
