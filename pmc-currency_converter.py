def currency_converter(rate,euros):
    dollars=euros*rate
    return dollars
r=input("Enter rate: ")
e=input("Enter euros: ")
result=currency_converter(float(r),float(e))
result=str(result)
msg='The converted amount is ' + result
print(msg)
