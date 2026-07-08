#check whether given number is armstring number or not

num = 153
og_num =num
arm = 0 
num_len = len(str(num))

while num >0:
    rem = num %10
    arm = arm +(rem**num_len)
    num=num//10
if og_num == arm:
    print("Armstrong Number")   
else:
    print("Not an Arm Strong Number")     