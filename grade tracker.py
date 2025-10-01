def get_grade_category(percentage):
    """Determines the grade category based on percentage."""
    if percentage >= 95-100:
        return "A"
    elif percentage >= 80-94:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

def grade_tracker():
    """Main function to run the grade tracker program."""
    try:
        num_subjects = int(input("Enter the number of subjects: "))
        if num_subjects <= 0:
            print("Invalid number of subjects. Exiting.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    
    grades = []
    
    for i in range(1, num_subjects + 1):
        while True:
            try:
                grade = float(input(f"Enter marks for subject {i}: "))
                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Please enter a valid grade (0-100).")
            except ValueError:
                print("Invalid input. Enter a number.")
    
    total_marks = sum(grades)
    percentage = total_marks / num_subjects
    grade_category = get_grade_category(percentage)
    highest_marks = max(grades)
    lowest_marks = min(grades)
    subjects_failed = sum(1 for mark in grades if mark < 50)
    subjects_passed = num_subjects - subjects_failed
    
    print(f"\nTotal Marks: {total_marks}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade_category}")
    print(f"Highest Marks: {highest_marks}")
    print(f"Lowest Marks: {lowest_marks}")
    print(f"Subjects that need improvement: {subjects_failed}")
    print(f"Subjects Passed: {subjects_passed}")
    print(f"Subjects Failed: {subjects_failed}")

grade_tracker()
