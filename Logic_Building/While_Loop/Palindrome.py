num = 123321
og_num = num

rev_num =0

while num > 0:
    rem= num%10
    rev_num = (rev_num * 10)+rem
    num = num //10
if rev_num == og_num:
    print("Palindrome") 
else:
    print("Not Palindrome")           