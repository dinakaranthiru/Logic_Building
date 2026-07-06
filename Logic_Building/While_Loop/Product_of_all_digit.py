num = 534
num_str = abs(num) 

prod = 1 

while num_str > 0:
    dig = num_str % 10
    prod = prod * dig
    num_str = num_str //10
print(prod)  