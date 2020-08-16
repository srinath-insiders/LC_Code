file_handler = None
try:
    file_handler = open("Working_with_files/test.txt")
    for line in file_handler:
        print(line)
except IOError:
    print("An IOError has occurred!")
finally:
    if file_handler is not None:
        file_handler.close()

print('-------------------------------------------------------------------')

try:
    with open("Working_with_files/test.txt") as file_handler:
        for line in file_handler:
            print(line)
except IOError:
    print(IOError)

    
print('-------------------------------------------------------------------')