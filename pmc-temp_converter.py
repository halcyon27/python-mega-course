def c_to_f(c):
    f=c*9/5+32
    return(f)

temperatures_c=[10,-20,-289,100]
for c in temperatures_c:
    if c > -273.15:
        print(c_to_f(c))
    else:
        print("That temperature is physically impossible!")
