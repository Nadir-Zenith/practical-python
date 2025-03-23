# mortgage.py
#
# Exercise 1.7

years = 30
mortgage = 500_000
interest_rate = 0.05
payment = 2684.11

extra_payment_start_month = 5 * 12
extra_payment_end_months = 12 * 9
extra_payment = 1000

total_sum = 0.0
months = 0

print(f'\t months \t\t total paid \t\t principal \n')
while mortgage > 0:
    months += 1
    monthly_payment = payment
    if extra_payment_start_month < months <= extra_payment_end_months:
        monthly_payment += extra_payment
        
    
    mortgage = mortgage * (1 +  interest_rate/12) - monthly_payment
    if mortgage < 0:
        total_sum += monthly_payment + mortgage
        mortgage -=  mortgage
    else:
        total_sum += monthly_payment

    print(f'\t {months} \t\t{total_sum:>8.3f} \t\t{mortgage:>8.3f}')

print(f'{total_sum=} ,in {months=}' )