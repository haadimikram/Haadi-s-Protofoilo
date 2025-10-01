def add_grade(grades):
    """Adds a new grade to the tracker."""
    subjects = ["Math", "Science", "History", "French", "Health & PE"]
    
    print("\nEnter your grades for the following subjects:")
    for subject in subjects:
        while True:
            try:
                grade = float(input(f"{subject}: "))
                if 0 <= grade <= 100:
                    grades[subject] = grade
                    break
                else:
                    print("Please enter a valid grade (0-100).")
            except ValueError:
                print("Invalid input. Enter a number.")

    print("\nGrades updated successfully!")

def view_grades(grades):
    """Displays all recorded grades."""
    if not grades:
        print("\nNo grades recorded yet.")
    else:
        print("\nYour Grades:")
        for subject, grade in grades.items():
            print(f"{subject}: {grade:.2f}%")

def calculate_average(grades):
    """Calculates and displays the average grade."""
    if not grades:
        print("\nNo grades recorded yet.")
        return
    
    average = sum(grades.values()) / len(grades)
    print(f"\nYour average grade: {average:.2f}%")

def grade_tracker():
    """Main function to run the grade tracker program."""
    grades = {}
    target_grade = 95 # Default target grade

    while True:
        print("\nOptions: add, view, average, set target, exit")
        action = input("What would you like to do? ").lower()

        if action == "add":
            add_grade(grades)
        elif action == "view":
            view_grades(grades)
        elif action == "average":
            calculate_average(grades)
        elif action == "set target":
            try:
                target_grade = float(input("Enter your target grade (0-100): "))
                if 0 <= target_grade <= 100:
                    print(f"Target grade set to: {target_grade:.2f}%")
                else:
                    print("Invalid input. Enter a number between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action == "exit":
            print("Goodbye! Keep working towards your goals!")
            break
        else:
            print("Invalid option. Try again.")
