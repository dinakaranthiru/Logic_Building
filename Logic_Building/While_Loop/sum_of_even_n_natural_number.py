# Calculate the sum of all even numbers from 1 up to n

n=100
total_sum = 0
counter = 2

while counter <=n:
    total_sum +=counter
    counter+=2
print('The even sum is :',total_sum)    