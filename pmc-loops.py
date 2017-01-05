## Loops
# for Loops
emails=['me@gmail.com', 'you@gmail.com', 'they@hotmail.com']
for email in emails:
    if 'gmail' in email:
        print(email)
a="Tricky"
for i in a[:3]:
    print(i)

# while Loops
password = ''
while password != 'python123':
    password=input('Enter password: ')
    if password == 'python123':
        print('We have a match')
    else:
        print('Sorry, try again!')

# for loop with multiple lists using zip
names=['james', 'john', 'phil']
domains=['gmail', 'hotmail', 'yahoo']
for n,d in zip(names,domains):
    print(i, j)
