# complex numbers are written with a "j" as the imaginary part

x = 3 + 5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# complex() function
# complex(real, imaginary)

x = complex(3, 5)

# converting a string into a complex number:

x = complex('3+5j')
print(x, "\n")

# doing math with a complex number from a string

z = complex("3+5j") # converting to complex number

print(z + 2) # add real number
print(z * (1 - 1j))
print(abs(z))
