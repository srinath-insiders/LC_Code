print('-------------------------------------------------------------------')

def a_function():
    print("You just created a function!")

a_function()    



def empty_function():
    pass

# pass statement. It is basically a null operation, which means that when pass is executed, nothing happens
empty_function()

print('-------------------------------------------------------------------')

def add(a, b):
    return a + b

print(add(1, 2)) # 3



# def add(a, b):
#    return a + b
# add(1)
# TypeError: add() takes exactly 2 arguments (1 given)

# add(c=5, d=2)

# TypeError: add() got an unexpected keyword argument 'c'

print('-------------------------------------------------------------------')


result = add(a=2, b=3) 
print(result) # 5

total = add(b=4, a=5)
print(total) # 9

print('-------------------------------------------------------------------')

def keyword_function(a=1, b=2):
    return a+b

result = keyword_function()
print(result) # 3

print('-------------------------------------------------------------------')

def mixed_function(a, b=2, c=3):
    return a+b+c

result = mixed_function(1, b=4, c=5)
print(result) # 10

result = mixed_function(1)
print(result) # 6

# result = mixed_function(b=4, c=5)
# TypeError: mixed_function() missing 1 required positional argument: 'a'

print('-------------------------------------------------------------------')

def many(*args, **kwargs):
    print(args)
    print(kwargs)

many(1, 2, 3, name="Mike", job="programmer")

# (1, 2, 3)
# {'job': 'programmer', 'name': 'Mike'}

print('-------------------------------------------------------------------')

def function_a():
    global a
    a = 1
    b = 2
    return a+b    

def function_b():
    c = 3
    return a+c

print(function_a())
print(function_b())