# This is a game where if a number is divisible by 3, then it will print "Fizz"
# If the number is divisible by 5 , then it will print "Buzz
# If the number is divisible by 5 and 3 , then it will print "FizzBuzz"
# If it doesn't meet the above conditions, then it will print the number.

# To print the welcome message
print("**Welcome to the FizzBuzz game**")

# Request the start and end numbers from the user

num1 = int(input("Enter the start number\n"))
num2 = int(input("Enter the ending number\n"))

# Use the for loop to loop through the start and end numbers and verify the conditions using if

for number in range(num1,num2+1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

