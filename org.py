# basketball
import random

# List of quotes
shoot_quotes = [
    "You made the game-winning shot!",
    "Swish! Nothing but net.",
    "Buckets! You're on fire!",
    "Clutch shot at the buzzer!"
]

teammate_quotes = [
    "You miss 100% of the shots you don't take.",
    "Teamwork makes the dream work.",
    "Pass it like a pro!",
    "Assist of the year right there!"
]

# Asking question
check = True
while check:
    ask = input("Teammate or shoot? Answer 'shoot' or 'teammate': ").lower()
    
    # Giving results based on the answer
    if ask == "shoot":
        print(random.choice(shoot_quotes))
        check = False
    elif ask == "teammate":
        print(random.choice(teammate_quotes))
        check = False
    else:
        print("Invalid input. Please type 'shoot' or 'teammate'.")

