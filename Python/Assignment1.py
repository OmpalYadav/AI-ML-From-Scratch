# Ask user for name and age
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hello", name, "you are", age, "years old!")

# Sum, difference, product, quotient
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

sum_result = a + b
difference = a - b
product = a * b
quotient = a / b

print("Sum =", sum_result)
print("Difference =", difference)
print("Product =", product)
print("Quotient =", quotient)

a="45"
b=int(a)
c=float(a)
d=str(a)

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

x = 10 + 3 * 2 ** 2
print(x)

#Write a program to swap values of two number

# Get input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Print numbers before swapping
print("\nNumbers before swapping:")
print("First Number:", num1)
print("Second Number:", num2)

# Swap the values using tuple assignment
num1, num2 = num2, num1

# Print numbers after swapping
print("\nNumbers after swapping:")
print("First Number:", num1)
print("Second Number:", num2)

celsius_input = input()
celsius_temp = float(celsius_input)
fahrenheit_temp = (celsius_temp * (9/5)) + 32
# print(fahrenheit_temp)

R=int(input("Enter The value of R "))
Area_cul=3.14 * R**2
Area_temp=float(Area_cul)
print(Area_temp)

#SI = (P ∗ R ∗ T)/100

P=int(input("Enter The Principal Amount "))
R=int(input("Enter The Interest rate "))
T=int(input("Enter Time Period "))

SI=float((P*R*T)/100)
print(SI)


#Decimal Convert
decimal_number = 45.78
integer_part = int(decimal_number) 
fractional_part = decimal_number - integer_part
print(integer_part)
print(fractional_part)
