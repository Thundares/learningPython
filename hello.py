print('Hello, world')

#input
a = int(input('Give me a number: '))
b = int(input('Give me another one: '))
print('\nTime to calculate\n')

#sum
sum = a + b
print('{aa} + {bb} = {soma}'.format(aa = a, bb = b, soma = sum))

#minus
minus = a - b
print('{aa} - {bb} = {soma}'.format(aa = a, bb = b, soma = minus))

#mult
mult = a * b
print('{aa} * {bb} = {soma}'.format(aa = a, bb = b, soma = mult))

#div
div = a / b
print('{aa} / {bb} = {soma}'.format(aa = a, bb = b, soma = div))

#mod
mod = a % b
print('{aa} % {bb} = {soma}'.format(aa = a, bb = b, soma = mod))

#if
print('\nTime to do a if condition\n')
if minus > 0:
    print('{aa} - {bb} is positive'.format(aa = a, bb = b))
else:
    print('{aa} - {bb} is negative'.format(aa = a, bb = b))

#loop
print('\nTime to loop')
for x in range(0,11):
    print('{i} * b == {bb}'.format(i = x, bb = b * x))

#list
listOne = [1,3,5,7,11,13,17,19]
print(listOne)
print('Position 2 = {}'.format(listOne[1]))
print('Position 5 = {}'.format(listOne[4]))
print('Max of list = {}'.format(max(listOne)))
print('Length of list = {}'.format(len(listOne)))

#method
def printTitle(text1):
    print('##########\n\n{}\n\n##########'.format(text1))
printTitle('Hello, Python')

#class
class FirstClass:
    def __init__(self):
        self.a = 50
        self.b = 80

    def whatDoesItContains(self):
        print('a = {}\nb = {}'.format(self.a, self.b))

usingClass = FirstClass()
usingClass.whatDoesItContains()