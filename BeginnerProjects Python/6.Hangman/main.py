
import random

word_list = ["aardvark", "baboon", "camel"]
selected_word= random.choice(word_list)
print(selected_word)

display=[]
### This is to generate a display with empty places with the same size of the word that is to be guessed ###
for letters in selected_word:
    display+="_"
print(display)

tries=5

guess=""

for j in range(len(selected_word)):
    guess= input("Please guess the letter: ").lower()
    for i in range(len(selected_word)):
        if(selected_word[i]==guess[0]):
            print(selected_word[i])
            display[i]=selected_word[i]
        else:
            tries-=1
    print(display)
