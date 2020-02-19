print("Let's do some Type Casting ")
# String to Float Numbers
print( "Add two numbers'")
num1 = input ("Enter 1st number = ")
num2 = input ("Enter 2nd number = ")
result1 = float(num1) + float(num2)
print(f"total value is = {result1}")

# Float to Integer Numbers
print("Let's Add 3.3 and 2.2 as integer and print the result 5, not 5.5 ")
result2 = int(3.3) + int(2.2)
print(f"total value is = {result2}")

# String to Float(num1, num2) and Float to Integer
print("Enter Float numbers and see the result as Integer")
num3 = input ("Enter 3rd number = ")
num4 = input ("Enter 4th number = ")
#Error if you uncomment following line|
#result3 = int(num3) + int(num4)
result3 = int(float(num3)) + int(float(num4))
print(f"total value is = {result3}")