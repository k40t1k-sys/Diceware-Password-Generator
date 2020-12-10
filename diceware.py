# Program to generate a password using dice-ware password generating algorithm.
# Ask the user how many words he wants in his password and program will generate
# that many words using the dictionary.

import time

# Implementation of random funtion.
# Not using pre built random library.

def random():
    x = time.thread_time_ns()
    a = 8974556217
    c = 524556445
    m = 2**32
    x = (a*x + c) % m
    return x


# Funtion to get the number after 5 dice rolls 
# to find the corresponding letter in the dictionary. 

def dicenumber():
    diceout = ""
    for i in range(5): # 5 dice rolls
        diceout += str((random() % 6) + 1) # Gives a random number between 1 to 6 and adds it to the diceout variable.
    return diceout


# Get the word corrresponding to the random number genrated from the 5 dice rolls.

def diceware(x):
    wordlist = open('dictionary.txt', 'r')
    for line in wordlist:
        if line.startswith(x):
            wordlist.close()
            return line.lstrip('123456\t')

# Ask the user for no. words to be present in the password.
# The more no of words present the more hard it is to break the code.

limit = int(input("How many words do you want in your password : "))

pswd = ''

for i in range(limit): 
    pswd += diceware(dicenumber()).strip('\n') + '-'

# Displaying the password using charachter seprated format.
# The charachter can be anything including a white space(' ') or a simple dash('-').

print(pswd.strip('-'))
