# Question 5: Calculate the sum of digits in number 12345

num = 12345
num_string = str(num)
sum=0

for i in num_string:
    sum += int(i)
    
print(f"Sun of digits : {sum}")