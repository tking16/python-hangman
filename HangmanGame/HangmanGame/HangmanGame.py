
from bs4 import BeautifulSoup
import urllib.request
import random

with urllib.request.urlopen('http://www.thefreedictionary.com/dictionary.htm') as response:
    html = response.read()

words = []
soup = BeautifulSoup(html, 'html.parser') # parses the html
item = soup.find("ul",class_="lst") #gets the block of random words

#Capture the words from the onlione dictionary
for word in item.find_all('li'):
    words.append(word.get_text())
print("Welcome to Hangman by Theo King")


answer = random.choice(words)
correct_letters = []
hidden_letters = []

for letter in answer:
    correct_letters.append(letter.lower())
    hidden_letters.append("_")

print(" ".join(hidden_letters))
attempts = 10

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
    elif player_guess not in correct_letters and player_guess.lower() != answer.lower():
        print("Sorry, try again :(")
        attempts -= 1

    if correct_letters == hidden_letters or player_guess.lower() == answer.lower():
        print("Congratulations! You win!")
        break

else:
    print("you lose, the answer was: " + answer.upper())
    print("potential words:")
    print(', '.join(words))