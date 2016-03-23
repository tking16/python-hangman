print("Welcome to Hangman by Theo King")

#variables for correct word
answer = "Testing"
correct_letters = []
hidden_letters = []


for letter in answer:
    correct_letters.append(letter)#.lower())
    hidden_letters.append("_")

print(" ".join(hidden_letters))


attempts = 5
while attempts > 0:
    print("Guesses left: " + str(attempts))

    player_guess = input("Enter a letter: \n")

    if player_guess in hidden_letters:
        print("Letter already submitted")
    elif player_guess in correct_letters:
        print("That's correct!")
        hidden_letters[correct_letters.index(player_guess)] = player_guess
        print(" ".join(hidden_letters))
    else:
        print("Sorry, try again :(")
        attempts -= 1
    if correct_letters == hidden_letters:
        print("Congratulations! You win!")
        break
else:
    print("you lose")