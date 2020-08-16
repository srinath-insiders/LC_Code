
handle = open(r"Working_with_files/test.txt", "r") # r specifies raw string
handle = open("Working_with_files/test.txt")

print('-------------------------------------------------------------------')

print("Working_with_files/test.txt")
# Working_with_files      est.txt

print('-------------------------------------------------------------------')

print(r"Working_with_files/test.txt")
# Working_with_files\test.txt

print('-------------------------------------------------------------------')

handle = open("Working_with_files/test.txt", "r")
data = handle.read()
print(data)
handle.close()

print('-------------------------------------------------------------------')

handle = open("Working_with_files/test.txt", "r")
data = handle.readline() # read just one line
print(data)
handle.close()

print('-------------------------------------------------------------------')

handle = open("Working_with_files/test.txt", "r")
data = handle.readlines() # read ALL the lines!
print(data)
handle.close()

print('-------------------------------------------------------------------')