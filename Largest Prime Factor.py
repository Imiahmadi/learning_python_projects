import math 

def prime(c): 
    prime = True
    for i in range(2, int(math.sqrt(c)+1)): 
        if c % i == 0: 
            prime = False
            break
    return(prime)

#x = 5
x = 600851475143
for i in range(0,x): 
    if prime(x): 
        print(x)
        break
    else: 
        x = x-1





# z = False
# for i in range(0,x): 
#     if prime(x-i): 
#         z = True
#         t = x-i
#     break







