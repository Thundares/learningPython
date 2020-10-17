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
index = 1
for x in range(a):
    print('{i} * b == {bb}'.format(i = index, bb = b * index))
    index += 1