import random

def result(inp, comp):
    if (inp==comp): return 0
    elif inp == 'r':
        return 1 if comp == 's' else 0;
    elif inp == 'p':
        return 1 if comp == 'r' else 0;
    elif inp == 's':
        return 1 if comp == 'p' else 0;

d = {"rock":"r", "paper":"p", "scissors":"s"}
rev = {v: k for k, v in d.items()}

def rps(inp):
    inp = inp.lower()
    if inp in d.keys(): inp = d[inp]

    if inp not in d.values():
       print("Invalid Input")
       return

    comp = random.choice(['r','p','s'])
    
    print(f"You played: {rev[inp]}")
    print(f"Computer played: {rev[comp]}")

    res = result(inp, comp)
    if res==0: print("YOU TIED!! :|")
    elif res==1: print("YOU WON!! :)")
    else: print("YOU LOST!! :(")

a = input("Enter Rock/Paper/Scissors (r/p/s): ")
rps(a)