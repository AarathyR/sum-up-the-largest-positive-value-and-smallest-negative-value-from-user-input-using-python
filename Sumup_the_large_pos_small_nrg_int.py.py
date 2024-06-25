# Initialize the largest positive and smallest negative
#Version: 1.1
#Errors: invalid literal for int() with base 10: '-' when int('-inf') was given
#Only float values can be used to represent an infinite integer
largest_positive = float('-inf')
smallest_negative = float('inf')

while True:
    #get the input from the user
    user_input = input("Enter a number or type 'done' to finish: ")
    
    #coverts srting value to clower case and checks it whether 'done'
    #string.lower() takes no arguments and returns the lowercased strings 
    #from the given string by converting each uppercase character to lowercase.
    if user_input.lower() == 'done':
        #quit from the loop
        break
    
    #if input is not 'done' using try to avoid error
    try:
        #convert the string to float
        number = float(user_input)
        
        #check if the acquired float value is greater than 0 and greater than largest_positive
        if number > 0 and number > largest_positive:
            #updates the largest_positive variable value
            largest_positive = number
        #check if the acquired float value is lesser than 0 and lesser than smallest_negative
        elif number < 0 and number < smallest_negative:
            #updates the smallest_negative variable value
            smallest_negative = number
    #if there is an value error print the error and continue
    except ValueError:
        print("Please enter a valid number or 'done' to finish.")
#if the largest_positive is equal to negative value or smallest_negative equal to a positive value then print Invalid input
if largest_positive == float('-inf') or smallest_negative == float('inf'):
    print("Invalid inputs to calculate the sum.")
#if the largest_positive is equal to a positive value or smallest_negative equal to a negative value then print the result
else:
    result = largest_positive + smallest_negative
    print(f"The sum of the largest positive value and the smallest negative value is:",largest_positive,'+',smallest_negative,'=', {result})