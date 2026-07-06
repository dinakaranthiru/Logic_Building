num = 534
num_str = abs(num) 

prod = 1 

while num_str > 0:
    dig = num_str % 10  #give last digit (eg:4)
    prod = prod * dig   #1*4
    num_str = num_str //10 #remove the last digit
print(prod)  