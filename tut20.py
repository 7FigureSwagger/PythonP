#Catching the error from the typecast if user tries to enter a string
try:
  number = int(input("Enter a number: "))
  print(number)
except ValueError as err:
  print("Invalid Input Value")