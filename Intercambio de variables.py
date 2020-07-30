#Una manera de hacerlo es esta:

#a = int(input('Digite el numero a: '))
#b = int(input('Digite el numero b: '))

#print(f"el nuevo valor de a es {b},\ny el nuevo valor de b es {a}.")


#otra forma

a = int(input('Digite el numero a: '))
b = int(input('Digite el numero b: '))

a,b = b,a #especificamos que a y b, son inversos.

print(f"el nuevo valor de a es {a},\ny el nuevo valor de b es: {b}")