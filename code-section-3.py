# get type type via type(input)
print(type("Hi"))

# convert data-type via data-type(input)
print(int(1.67))
a=int(1.67)

## math operations: celsius to fahrenheit
def c_to_f(c):
    f=c*9/5+32
    return(f)
print(c_to_f(10))

## string operations:
# convert to int:
int('7')

# string indexing
day='friday'
print(day[:3]+day[-3:])

## list opperations
# assign
li=['one', 'monkey', 'crazy']
# read
print li[2]
# delete
del li[3]
# math
li[2]*2
# append, insert, remove, etc (dir(li))
li.append('wow')
li.remove('wow')
li.insert(0, 'first item')

## Tuples
# Like lists, but immutable; used for looking through object, for instance buttons in a gui
t=(1,2,3)

## Dictionaries
# like a list, but user must index via keys and values pairs
dict={"name":"aden","job":"QA"}
dict.values()
dict.keys()
dict_to_list=list(dict)

## Section 3 task
# print 10 from the following: money={"saving_account":200, "checking_account":100, "under_bed":[500,10,100]}
money={"saving_account":200, "checking_account":100, "under_bed":[500,10,100]}
money['under_bed'][1]
