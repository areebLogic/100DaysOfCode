
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
selected_word= random.choice(word_list)
guess=""
print(selected_word)

display=[]
### This is to generate a display with empty places with the same size of the word that is to be guessed ###
for letters in selected_word:
    display+="_"
print(display)

tries=6


# A nested loop is being used, the outer loop will run till whe word is successfully completed or
# until the player has exhausted the tries.
game_end= False


while not game_end:
    
    guess= input("Please guess the next letter: ").lower()
    for i in range(len(selected_word)):
        
        if guess not in selected_word:
            tries-=1
            if tries>0:
                print(stages[tries])
                print("Wrong letter, try again")
                break
            else:
                print(stages[0])
                print("You've lost the game")
                game_end= True
                break
        elif(selected_word[i]==guess[0]):
            display[i]=selected_word[i]
            if "_" not in display:
                game_end= True
                print("You won the game!!")
    print(display)