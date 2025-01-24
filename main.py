import random 
random_words=["bad","ball","window"]
lives=6
wrong_letters=[]

#ramdom choice
random_word=random.choice(random_words)

#store hangman stages ascii
hangman_stages= ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#see the user number of letters and pic of hangman
display=["-"]*len(random_word)
print(" ".join(display))
print(hangman_stages[0])

#while loop for guessing 
while "-" in display and lives>0:
  guessed_letter=input("Please guess a letter \n").lower()
  if guessed_letter in wrong_letters:
    print("you alreday guessed that .Try again")
    print("You have ",lives,"lives left")
    continue

  for positions in range(len(random_word)):
    if random_word[positions]==guessed_letter:
      display[positions]=guessed_letter
      print(display)
      print("You have",lives,"more lives")
  
  if guessed_letter not in random_word:
     wrong_letters.append(guessed_letter)
     if guessed_letter in wrong_letters:
        print("Wrong guess")
        lives=lives-1
        print("You have",lives,"lives left")
    
  print(hangman_stages[6-lives])

#Wining or losing

if lives==0:
  print("You lose")
  #print(hangman_stages[-1])

else:
  print("You win")
 