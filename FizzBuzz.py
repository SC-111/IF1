def num_checker(input_value):
    if input_value % 3 == 0 and input_value % 5 == 0:
        return "FizzBuzz"
    elif input_value % 5 == 0:
        return "Buzz"
    elif input_value % 3 == 0:
        return "Fizz"
    else:
        return str (input_value)
    

print (num_checker (-30))

# success 

