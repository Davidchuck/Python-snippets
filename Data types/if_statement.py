#house price
value=1000000
good_credit_score=True

if good_credit_score:
    down_payment=0.1*value
    print("You need to put down a 10% downpayment")
    print(f"Downpayment: ${down_payment}")
else:
    down_payment=0.2*value
    print("You need to put down a 20% downpayment")
    print(f"Downpayment: ${down_payment}")
