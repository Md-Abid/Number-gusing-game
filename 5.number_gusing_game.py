import random
n=random.randint(0,100)
number_of_guesses=1
name=input("Enter a number: ")
name=name.upper()
print(f"Hello {name}. Let's began the number gusing game.")
print("Remember: Number of guesses is limited to only 10 times.")
print("\n")
while (number_of_guesses<=10):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<n:
        print(f"{name} you enter less number please input greater number.\n")
    elif guess_number>n:
        print(f"{name} you enter greater number please input smaller number.\n ")
    else:
        print(f"Horray {name}! you won\n")
        print(number_of_guesses,"no.of guesses you took to finish.")
        break
    print(10-number_of_guesses,"no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>10):
    print(f"Sorry {name}! You lost.")
    print("Game Over")
  
