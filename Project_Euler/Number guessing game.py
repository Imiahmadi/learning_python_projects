

import random 

r = random.randint(0,100)

print("number of guesses is 7, be careful")
print("----------------------------------") 
print(f"answer = {r}")

guess = 0
while guess < 7: 

    print(f"you have {7-guess} chances to guess")
    x = int(input("give the guess"))
    guess += 1  

    if x == r: 
        print("nice, your answer is exact true!")
        break 

    elif x < r: 
        print("answer is highr!")
    
    elif x > r: 
        print("answer is lower!")
