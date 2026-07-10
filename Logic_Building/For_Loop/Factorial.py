#using for loop
num = 5
fac = 1

for i in range(1,num+1):
    fac *=i
    
print(fac)    

#using function
def fact(n):
    if n ==0 or n==1:
        return 1
    return n*fact(n-1)
print(fact(5))


