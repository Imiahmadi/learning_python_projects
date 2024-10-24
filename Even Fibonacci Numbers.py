

n = 0
a = 1
b = 2

# for i in range(1,10): 
#     n = a + b 
#     a = b
#     b = n

#     if b < 90:
#         print(b)
sum = 0 
while n < 3999999: 
    n = a + b 
    a = b
    b = n
    
    if n % 2 == 0:
        sum = sum + n

print(sum)


    
