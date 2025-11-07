# String repetition using multiplication with integers
A, B = 2, 3
Txt = "@"
print(2 * Txt * 3)

# String concatenation after converting integer to string
A, B = 2, 3
Txt = "@"
print((str(A) + Txt) * B)

# Arithmetic operations with operator precedence
A, B = 2, 3
C = 4
print(A + B * C)

# Integer multiplied by float gives float result
A, B = 10, 5.0
C = A * B
print(C)

# Division between two integers gives float result
A, B = 1, 3
C = A / B
print(C)

# Floor division and normal division with float numerator
A, B = 1.5, 3
C = A // B
print(C, A / B)

# Floor division with positive integers
A, B = 12, 5
C = A // B
print(C)

# Floor division with negative numerator
A, B = -12, 5
C = A // B
print(C)

# Modulo with negative numerator and positive denominator
A, B = -12, 5
C = A % B
print(C)

# Modulo with both numerator and denominator negative
A, B = -12, -5
C = A % B
print(C)

# Modulo with positive numerator and denominator
A, B = 5, 2
C = A % B
print(C)

# Modulo with positive numerator and negative denominator
A, B = 5, -2
C = A % B
print(C)
