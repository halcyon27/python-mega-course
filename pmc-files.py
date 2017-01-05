## File handling

# r - opens for read only; pointer at beginning of file
# r+ - opens for read/write. pointer at beginning of file
# w - opens for write. overwrites file if it already exists
# w+ - opens for read/write. overwrites file if it already exists
# a - opens for append. on existing file, pointer begins at eof. creates if needed
# a+ - opens file for read/append. creates if needed

# open and read
f=open('example.txt', 'r')
# set string variable as content of f
content=f.read()
print(content)
# reset location within f
f.seek(0)
# set list variable as content of f, inlcuding \n
content=f.readlines()
print(content)
# strip line endings
content=[i.rstrip('\n') for i in content]
print(content)
f.close(f)
# create and write
f=open('example2.txt','w')
f.write('Line 1\n')
f.write('Line 2')
f.close()

# append lines to existing File
f=open('example.txt', 'a')
file.write('Line 7')
file.close()

# with block (no close method needed)
with open('example.txt','a+'') as f:
    content=file.read()
    f.write('foo\n')

# write temps in loop

temperatures=[10,-20,-289,100]

def writer(temperatures):
    with open("temps.txt", 'w') as file:
        for c in temperatures:
            if c>-273.15:
                f=c*9/5+32
                file.write(str(f)+"\n")

writer(temperature) #Here we're calling the function, otherwise no output will be generated
