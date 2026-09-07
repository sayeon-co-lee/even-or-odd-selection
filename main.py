# Even or Odd

## Ask the user for a whole number
number = int(input("Enter a number: "))

## Check if the number is divisible by 2 
if number % 2 == 0:
    print (f"{number} is even.")
else:
    print (f"{number} is odd.")