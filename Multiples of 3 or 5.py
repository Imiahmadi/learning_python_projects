

# first we should find multiple numbers of 3 or 5



def m(n):
    m = False
    if n % 3 == 0 or n % 5 == 0:
        m = True
    return m

sum = 0 
for i in range(0,1000): 
    if m(i):
        sum = sum + i 

print(sum)

