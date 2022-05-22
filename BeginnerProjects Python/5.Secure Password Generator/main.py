import numbers
import random

passwordLength=int(input("How many characters should your desired password have?"))

lower_case= "abcdefghijklmnopqrstuvwxyz"
upper_case= lower_case.upper()
special_chars= "~`!@#$%^&*\/;:"
numberz = "0123456789"

selection_chars = lower_case + upper_case + special_chars + numberz
password = "".join(random.sample(selection_chars,passwordLength))

print("Your password has been generated! Your password is: ")
print(password)
