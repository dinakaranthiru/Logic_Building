# # Calculate and print the factorial of a given number.
# Print all numbers from 1 to 10 using a loop.
# 2. Print numbers from 10 down to 1 in reverse order.
# 3. Print all even numbers between 1 and 100.
# 4. Print all odd numbers between 1 and 100.
# 5. Print the multiplication table of a given number from n × 1 to n × 10.
# 6. Calculate and print the sum of the first n natural numbers.
# 7. Calculate the sum of all even numbers from 1 up to n.
# 8. Calculate the sum of all odd numbers from 1 up to n.


# n = 1
# while n <11:
#     print(n)
#     n+=1    

# n = 10
# while n >=1:
#     print(n)
#     n=n-1

# n = 2
# while n <101:
#     print(n)
#     n=n+2
  
# n = 1
# while n <101:
#     print(n)   
#     n=n+2 

# n = 1
# while n<11:
#     print(f"{n} x 5 = {n*5}")
#     n = n+1

# n=100
# total_sum = 0
# counter = 1

# while counter <=n:
#     total_sum +=counter
#     counter = counter+1
# print(total_sum) 

   
# n=100
# total_sum = 0
# counter = 2

# while counter <=n:
#     total_sum +=counter
#     counter = counter+2
# print(total_sum) 
   
# n=100
# total_sum = 0
# counter = 1

# while counter <=n:
#     total_sum +=counter
#     counter = counter+2
# print(total_sum)    

n = 5
res = 1

while n >1:
    res = res *n
    n = n-1
print(res)       