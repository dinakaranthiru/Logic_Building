#Check whether the given number is a Perfect number

num = 28
div = 1
sum_of_div = 0

while div < num:
    if num % div == 0:
        sum_of_div += div
    div +=1
        
 
 
if sum_of_div == num:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")