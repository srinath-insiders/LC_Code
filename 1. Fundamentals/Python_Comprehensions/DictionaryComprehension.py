print('-------------------------------------------------------------------')

print( {i: str(i) for i in range(5)} )
# {0: '0', 1: '1', 2: '2', 3: '3', 4: '4'}

print('-------------------------------------------------------------------')

my_dict = {1:"dog", 2:"cat", 3:"hamster"}
print( { value:key for key, value in my_dict.items()} )

print('-------------------------------------------------------------------')

# This will only work if the dictionary values are of a non-mutable type, 
# such as a string. Otherwise you will end up causing an exception to be raised.