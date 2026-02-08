# Question 3: Calculate the compound interest on $1000 at 5.5% for 3 years

principal = 1000
rate = 5.5
time = 3

amount = principal*(1 + rate / 100)** time
compound_interest = amount - principal

print(f"compound_interest : ${compound_interest:.2f}")