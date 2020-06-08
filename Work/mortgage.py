# mortgage.py
#

# Exercise 1.9

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment = 1000.0
extra_payment_start_month = 60
extra_payment_end_month = 108


while principal > 0:
    month += 1
    principal = principal * (1 + rate/12) - payment
    total_paid = total_paid + payment
    
    if month >= extra_payment_start_month and month < extra_payment_end_month:
        principal = principal  -  extra_payment
        total_paid = total_paid + extra_payment
        
    print(month, round(total_paid,2), round(principal,2))

print('Total paid', round(total_paid,2))
print('Months', month)

s = f'Total paid:${total_paid:0.2f}  Months:{month}.'
print(s)






# Exercise 1.8
'''
principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment = 1000
total_paid = 0.0
month = 0

while principal > 0:
    month += 1
    principal = principal * (1 + rate/12) - payment
    total_paid = total_paid + payment
    
    if month >= extra_payment_start_month and month < extra_payment_end_month:
        principal = principal  -  extra_payment
        total_paid = total_paid + extra_payment

print('Total paid', round(total_paid,2))
print('Months', month)

'''


# Exercise 1.7

'''
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

while principal > 0:
    principal = principal * (1 + rate/12) - payment
    total_paid = total_paid + payment

print('Total paid', round(total_paid,1))

'''


