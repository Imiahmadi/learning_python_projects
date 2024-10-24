
# n = 12
# for i in range(1,n): 
#     for j in range(1,n): 
#         for k in range(1,n): 
#             if i + j + k == n and (i**2 + j**2) == k**2: 
#                 print(i, j, k)


for a in range(1000):
        for b in range(1000-a):
           c = 1000-a-b
           if a**2 + b**2 == c**2:
               print (a,b,c)
         
           
