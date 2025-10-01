def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    return fibonacci_sequence[:n]

def is_in_fibonacci(number, sequence):
    return number in sequence

def main():
    print("Welcome to the Fibonacci Explorer!")
    num_terms = int(input("How many terms of the Fibonacci sequence would you like to generate? "))
    
    fibonacci_sequence = generate_fibonacci(num_terms)
    print("\nFibonacci Sequence:")
    print(", ".join(map(str, fibonacci_sequence)))
    
    while True:
        user_number = int(input("\nEnter a number to check if it's in the Fibonacci sequence: "))
        if is_in_fibonacci(user_number, fibonacci_sequence):
            print(f"Yes! {user_number} is in the Fibonacci sequence.")
        else:
            print(f"No, {user_number} is not in the Fibonacci sequence.")
        
        another_check = input("\nEnter another number to check? (yes/no): ").strip().lower()
        if another_check != "yes":
            break

if __name__ == "__main__":
    main()
