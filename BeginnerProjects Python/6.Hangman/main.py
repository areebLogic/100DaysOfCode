from asyncio import selector_events
import random
from select import select

word_list = ["aardvark", "baboon", "camel"]


selected_word= random.choice(word_list)
print(selected_word)
guess= input("Please guess the word: ").lower()

if(selected_word==guess):
    print("You're right")
else:
    print("You're wrong")