handle = open("Writing_Files/test.txt","w")
handle.write("This is just a test")
handle.close()

handle = open("Writing_Files/test.txt","r")
while True:
    data = handle.read(1024)
    print(data)
    if not data:
        break


print('-------------------------------------------------------------------')


# Python has a neat little builtin called with which you can use to simplify reading 
# and writing files. The with operator creates what is known as a context manager in Python 
# that will automatically close the file for you when you are done processing it

with open("Writing_Files/test.txt") as file_handler:
    for line in file_handler:
        print(line)
