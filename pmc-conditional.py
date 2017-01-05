## conditionals
# in block form
v=0
if v>3:
    print("less")
elif v==3:
    print("it's equal")
else:
    print("Equal or greater")

# inline conditionals
print("positive v" if v>0 else v==0 "null v" else "negative v")
