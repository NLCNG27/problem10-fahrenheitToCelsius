# Author: Nguyen L.
# Date: May 12th, 2020
# Write a program to convert Fahrenheit to Celsius
# Formula: C = (F - 32) * (5/9)

def convert(fahrenheit):

    # utilize formula
    celsius = (fahrenheit - 32) * (5/9)

    return celsius

result = int(input("Enter Fahrenheit to convert: "))
print("Result: " + str(convert(result)))