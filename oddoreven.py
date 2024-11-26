import random

def odd_or_even_game():
    print("Welcome to the Odd or Even Hand Game!")
    print("You will play against the computer.")
    print("Rules: Choose either odd or even. Show a number of fingers (0 to 5).")
    print("If the sum of your fingers and the computer's fingers matches your choice, you win!")

    user_choice = input("Do you choose 'odd' or 'even'? ").lower()
    while user_choice not in ["odd", "even"]:
        user_choice = input("Invalid choice. Please choose 'odd' or 'even': ").lower()

    try:
        user_fingers = int(input("How many fingers will you show? (0 to 5): "))
        if user_fingers < 0 or user_fingers > 5:
            raise ValueError
    except ValueError:
        print("Invalid input! Please enter a number between 0 and 5.")
        return

    computer_fingers = random.randint(0, 5)
    print(f"The computer showed {computer_fingers} fingers.")

    total = user_fingers + computer_fingers
    result = "even" if total % 2 == 0 else "odd"
    print(f"The total is {total}, which is {result}.")

    if user_choice == result:
        print("Congratulations! You win!")
    else:
        print("Sorry, you lose. Better luck next time!")

odd_or_even_game()
