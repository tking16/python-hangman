print("Welcome to Hangman by Theo King")

#variables for correct word
answer = "Jujimufu"
correct_letters = []
hidden_letters = []

for letter in answer:
    correct_letters.append(letter.lower())
    hidden_letters.append("_")

print(" ".join(hidden_letters))
attempts = 5

while attempts > 0:
    print("Guesses left: " + str(attempts))
    count = -1 
    player_guess = input("Enter a letter: \n")
    if player_guess in hidden_letters:
        print("Letter already submitted")  
    elif player_guess in correct_letters:
        print("That's correct!")
        for letter in correct_letters:
            count += 1
            if player_guess == letter:
                hidden_letters[correct_letters.index(player_guess,count)] = player_guess
        print(" ".join(hidden_letters))
    elif correct_letters == hidden_letters or player_guess.lower() == answer.lower():
            print("Congratulations! You win!")
            break
    else:
        print("Sorry, try again :(")
        attempts -= 1

else:
    print("you lose")