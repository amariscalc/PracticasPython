# Challenges
'''
Write a program that shows by console (with a print) the numbers from 1 to 100.
Replaces the following:
· Multiples of 3 changed to "Fizz"
· Multiples of 5 changed to "Buzz"
· Multiples of 3 and 5 change to "FizzBuzz"
'''
# Function to check the number
def is_fizz_buzz (number):
    
    if number % 3 ==0:
        
        if number % 5 == 0:
            return "FizzBuzz"
        else:
            return "Fizz"
    
    elif number % 5 == 0:
        return "Buzz"
    
    else:
        return str (number) 

#main ()
# Create a list
other_fizz_buzz_list = [i for i in range(1,101)]

# Run the for loop and check the number by "other_fizz_buzz_list" function
for i in other_fizz_buzz_list:
    print(is_fizz_buzz(i))