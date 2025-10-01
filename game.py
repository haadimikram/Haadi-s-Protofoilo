import random
import pyttsx3
import speech_recognition as sr
import time

engine = pyttsx3.init()
recognizer = sr.Recognizer()

# Voice settings
engine.setProperty('rate', 160)  # Clearer speed
engine.setProperty('volume', 1.0)  # Full volume
voices = engine.getProperty('voices')
if voices:
    engine.setProperty('voice', voices[0].id)  # Use first available voice

# Characters from book
characters = ["Cam", "Daphne", "Chuck", "Mr. Fanshaw", "Zara"]

# Game board spaces
board_spaces = [
    "Start",
    "Play Video Games",
    "Start a Club",
    "Trivia Time",
    "Talk Your Way Out",
    "Clean-Up Duty",
    "Pretend to Help"
]

# Trivia Questions
trivia_questions = [
    {
        "question": "Why did Cam start the P.A.G. club?",
        "options": ["A. He loved helping", "B. To avoid punishment", "C. Daphne made him"],
        "answer": "B"
    },
    {
        "question": "Who is most suspicious of Cam?",
        "options": ["A. Daphne", "B. Mr. Fanshaw", "C. Chuck"],
        "answer": "A"
    },
]

players = []

def speak(text):
    print(f"\n🎤 SPEAKING: {text}")
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.4)

def listen_for_command(prompt):
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        speak(prompt)
        print("🎧 Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"🎙️ You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, speech service is unavailable.")
        return ""

def ask_trivia(player):
    q = random.choice(trivia_questions)
    speak(f"{player['name']}, it's trivia time!")
    speak(q["question"])
    for option in q["options"]:
        speak(option)
    answer = listen_for_command("Please say your answer: A, B, or C.")
    if answer and answer[0].upper() == q["answer"]:
        speak("Correct! Plus one point.")
        player['points'] += 1
    else:
        speak("Wrong answer. No points.")

def do_space_action(space, player):
    speak(f"{player['name']} landed on {space}.")
    actions = {
        "Trivia Time": lambda: ask_trivia(player),
        "Play Video Games": lambda: speak("You got distracted playing games. No points."),
        "Start a Club": lambda: speak("You started a club! Nice effort, but no points."),
        "Pretend to Help": lambda: speak("You pretended to help... but we know."),
        "Talk Your Way Out": lambda: speak("You avoided trouble with clever words."),
        "Clean-Up Duty": lambda: speak("You cleaned up a mess. Gross, but someone had to."),
        "Start": lambda: speak("The journey begins!")
    }
    actions.get(space, lambda: speak("Nothing happens."))()

def get_dice_number(player_name):
    while True:
        dice_input = listen_for_command(f"{player_name}, say the number you rolled on the dice.")
        try:
            dice = int(dice_input)
            if 1 <= dice <= 6:
                print(f"🎲 RESULT: {player_name} rolled a {dice}")
                return dice
            else:
                speak("Please say a number between 1 and 6.")
        except ValueError:
            speak("That wasn't a number. Try again.")

def setup_players():
    number_words = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "1": 1, "2": 2, "3": 3, "4": 4, "5": 5
    }

    speak("How many players are playing? You can have up to 5 players.")

    while True:
        count_input = listen_for_command("Say a number from 1 to 5.")
        count_input = count_input.lower().strip()
        
        if count_input in number_words:
            num_players = number_words[count_input]
            break
        else:
            speak("Sorry, I didn't understand. Please say a number from one to five.")

    chosen_characters = []
    for i in range(num_players):
        while True:
            speak(f"Player {i + 1}, choose your character:")
            for char in characters:
                speak(char)
            choice = listen_for_command("Say the name of the character you want.")
            if choice:
                matched = [c for c in characters if c.lower() == choice.lower()]
                if matched and matched[0] not in chosen_characters:
                    player = {
                        "name": matched[0],
                        "position": 0,
                        "points": 0
                    }
                    players.append(player)
                    chosen_characters.append(matched[0])
                    speak(f"{matched[0]} selected.")
                    break
                else:
                    speak("That character is already taken or not valid. Try again.")
            else:
                speak("Please say a character name.")

def show_scores():
    print("\n📊 SCOREBOARD:")
    for player in players:
        print(f"{player['name']}: {player['points']} point(s)")

def main():
    speak("Welcome to the Slacker board game voice assistant!")
    setup_players()

    while True:
        for player in players:
            speak(f"{player['name']}, it's your turn.")
            dice = get_dice_number(player['name'])
            player['position'] = (player['position'] + dice) % len(board_spaces)
            current_space = board_spaces[player['position']]
            do_space_action(current_space, player)
            speak(f"{player['name']} now has {player['points']} point(s).")

        show_scores()
        cmd = listen_for_command("Say 'continue' to play another round, or 'quit' to end the game.")
        if "quit" in cmd:
            break

    speak("Game over! Here are the final scores:")
    show_scores()
    speak("Thanks for playing!")

if __name__ == "__main__":
    main()
