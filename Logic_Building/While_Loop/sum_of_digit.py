#sum of n natural number
# num = 100

# total= 0
# counter = 1

# while counter <=num:
#     total = total+counter
#     counter=counter+1
# print(total) 

#Find and print the sum of digits of the given number 
   
num = 2345

sum_of_digit = 0

while num>0:
    rem = num % 10
    sum_of_digit = sum_of_digit+rem
    num = num //10
print(sum_of_digit)        