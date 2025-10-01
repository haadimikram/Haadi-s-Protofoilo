import random
import pyttsx3
import speech_recognition as sr
import time

# Initialize text-to-speech and recognizer
engine = pyttsx3.init()
recognizer = sr.Recognizer()

# Player stats
xp = 0
clubs = 0
points = 0

# Game board
spaces = [
    "Start", "Play Video Games", "Start a Club", "Trivia Time",
    "Principal's Office", "Community Service", "Pretend to Help",
    "Trivia Time", "Play Video Games", "Principal's Office"
]

# Trivia questions
trivia_questions = [
    {
        "question": "Why did Cam start the P.A.G. club?",
        "options": ["A. He loved helping", "B. To avoid punishment", "C. Daphne made him"],
        "answer": "b"
    },
    {
        "question": "Who is most suspicious of Cam?",
        "options": ["A. Daphne", "B. Mr. Fanshaw", "C. Chuck"],
        "answer": "a"
    },
    {
        "question": "What is Cam's favorite activity?",
        "options": ["A. Soccer", "B. Eating", "C. Playing video games"],
        "answer": "c"
    },
    {
        "question": "What does P.A.G. stand for?",
        "options": ["A. Perfect Awesome Gamers", "B. Positive Action Group", "C. People Against Gaming"],
        "answer": "b"
    },
    {
        "question": "Which animal causes a big problem in the story?",
        "options": ["A. Hamster", "B. Beaver", "C. Squirrel"],
        "answer": "b"
    },
    {
        "question": "Who accidentally becomes a hero in the book?",
        "options": ["A. Cam", "B. Pavel", "C. Daphne"],
        "answer": "a"
    },
    {
        "question": "Why does the P.A.G. get popular?",
        "options": ["A. Cam's speech", "B. Students want volunteer hours", "C. The principal promotes it"],
        "answer": "b"
    },
    {
        "question": "Who is Cam’s best friend?",
        "options": ["A. Chuck", "B. Pavel", "C. Benny"],
        "answer": "a"
    },
    {
        "question": "Where does Cam spend most of his time?",
        "options": ["A. Library", "B. Outside", "C. His basement"],
        "answer": "c"
    },
    {
        "question": "What game does Cam play a lot?",
        "options": ["A. Zombie Destroyer", "B. WarCraft", "C. League of Legends"],
        "answer": "a"
    },
    {
        "question": "Who forces Cam to attend a meeting?",
        "options": ["A. His mom", "B. Mr. Fanshaw", "C. Daphne"],
        "answer": "c"
    },
    {
        "question": "What happens to the beaver?",
        "options": ["A. It attacks the class", "B. It gets rescued", "C. It destroys the school"],
        "answer": "b"
    },
    {
        "question": "Cam becomes famous for what?",
        "options": ["A. Starting clubs", "B. Saving a beaver", "C. Pretending to volunteer"],
        "answer": "b"
    },
    {
        "question": "What’s Cam’s goal in the book?",
        "options": ["A. Help the community", "B. Avoid getting grounded", "C. Get good grades"],
        "answer": "b"
    },
    {
        "question": "How does Cam change by the end?",
        "options": ["A. He becomes a real helper", "B. He stays lazy", "C. He moves schools"],
        "answer": "a"
    },
]

# Voice functions
def speak(text):
    print("🎙️", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("🎤 Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            response = recognizer.recognize_google(audio).lower()
            print("🗣️ You said:", response)
            return response
        except:
            speak("Didn't catch that. Try again.")
            return ""

# Game turn
def take_turn():
    global xp, clubs, points
    roll = random.randint(1, 6)
    space = spaces[roll % len(spaces)]
    speak(f"You rolled a {roll} and landed on {space}.")

    if space == "Play Video Games":
        xp += 10
        speak("You played video games. XP +10.")
    elif space == "Start a Club":
        clubs += 1
        speak(f"You started club #{clubs}. That sounds... productive?")
    elif space == "Community Service":
        points += 1
        speak("You did community service! +1 Good Boy Point.")
    elif space == "Principal's Office":
        points = max(0, points - 1)
        speak("Oops. You got caught. -1 Good Boy Point.")
    elif space == "Pretend to Help":
        speak("You pretended to help. Nothing happened.")
    elif space == "Trivia Time":
        ask_trivia()

    speak(f"📊 XP: {xp}, Clubs: {clubs}, Points: {points}")
    time.sleep(1)

# Trivia system
def ask_trivia():
    q = random.choice(trivia_questions)
    speak(q["question"])
    for option in q["options"]:
        speak(option)
    speak("Say A, B, or C for your answer.")

    answer = listen()
    if q["answer"] in answer:
        speak("Correct! +1 point.")
        global points
        points += 1
    else:
        speak("Wrong answer. Better luck next time.")

# Game loop
def start_game():
    speak("Welcome to Slacker: The Voice Board Game. Say 'roll' to begin or 'quit' to exit.")
    while True:
        speak("Your move. Say 'roll' or 'quit'.")
        user_input = listen()
        if "roll" in user_input:
            take_turn()
        elif "quit" in user_input:
            speak("Thanks for playing Slacker. See you next time!")
            break
        else:
            speak("Say 'roll' or 'quit'.")

# Start the game
start_game()
