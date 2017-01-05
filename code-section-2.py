# Notes from: Python-Mega-Course
# FUNCTIONS
# def to define a function; input passed in brackets
def currency_converter(rate,euros):
	dollars=euros*rate
	return dollars
	
print(currency_converter(100,1000))
# HELP
# help(function) == assistance on the named function
# dir(object) == available methods to apply to the named object
# help(object.method) == help on method: help(str.replace)