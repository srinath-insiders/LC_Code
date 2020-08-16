print('-------------------------------------------------------------------')

x = [i for i in range(5)]
print(x)

print('-------------------------------------------------------------------')

line = ["SOME TERM "," Srinath "," SOME TERM Maaama ", " Swathi ", " Rupa "]
ans_line = [i for i in line if "SOME TERM" in i]
print(ans_line)

print('-------------------------------------------------------------------')

x = ['1', '2', '3', '4', '5']
y = [int(i) for i in x]
print(y) # [1, 2, 3, 4, 5]

print('-------------------------------------------------------------------')

myStringList = [
  '    Hello how are you?',
  'I\'m good    ',
  '    I\'m good too   ']
myStrings = [s.strip() for s in myStringList]
print(myStrings)

print('-------------------------------------------------------------------')

vec = [[1,2,3], [4,5,6], [7,8,9]]
flatVec = [element for num in vec for element in num]
print(flatVec) # [1, 2, 3, 4, 5, 6, 7, 8, 9]