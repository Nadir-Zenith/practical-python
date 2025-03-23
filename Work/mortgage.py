# mortgage.py
#
# Exercise 1.7

years = 30
mortgage = 500_000
interest_rate = 0.05
payment = 2684.11
total_sum = 0.0
months = 0

while mortgage > 0:
    months += 1
    monthly_payment = payment
    if months <= 12:
        monthly_payment += 1000
        
    total_sum += monthly_payment
    mortgage = mortgage * (1 +  interest_rate/12) - monthly_payment
    

print(f'{total_sum=} ,in {months=}' )