# mortgage.py
#
# Exercise 1.7
# mortgage.py
principal = 500000.0
rate = 0.05
base_payment = 2684.11
total_paid = 0.0
month = 0
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    principal = principal * (1+rate/12)
    if extra_payment_start_month <= month <= extra_payment_end_month:
        payment = min(base_payment+extra_payment, principal)
    else:
        payment = min(base_payment, principal)
    principal -= payment
    total_paid =  round(total_paid + payment, 2)
    month += 1
    print(f'{month: 5d}, {total_paid: 10.2f}, {principal: 10.2f}')

print('Total paid {} \n Months {}'.format(total_paid, month))
