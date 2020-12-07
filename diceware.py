import time

def random():
    x = time.thread_time_ns()
    a = 8974556217
    c = 524556445
    m = 2**32
    x = (a*x + c) % m
    return x

def dicenumber():
    diceout = ""
    for i in range(5): # 5 dice rolls
        diceout += str((random() % 6) + 1) # add result of dice roll to variable
    return diceout

def diceware(x):
    wordlist = open('dictionary.txt', 'r')
    for line in wordlist:
        if line.startswith(x):
            return line.lstrip('123456\t')

limit = int(input("How maany words do you want in your password : "))

pswd = ''

for i in range(limit): 
    pswd += diceware(dicenumber()).strip('\n') + '-' # increase number for longer passphrases



print(pswd.strip('-'))