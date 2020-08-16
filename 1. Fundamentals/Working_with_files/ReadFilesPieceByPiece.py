print('-------------------------------------------------------------------')
handle = open("Working_with_files/test.txt", "r")

for line in handle:
    print(line)

handle.close()

print('-------------------------------------------------------------------')

handle = open("Working_with_files/test.txt","r")

while True:
    data = handle.read(1024)
    print(data)
    if not data:
        break

print('-------------------------------------------------------------------')

# handle = open("Working_with_files/test.pdf","r")
# Reading a binary file. So this time we changed the file mode to rb
