def test_pytest():
    2 + 2 == 4

from FizzBuzz import num_checker

#testing Fizz 

def test_fizz():
    assert num_checker(3) == "Fizz" # using known multiples of 3 to test Fizz element of function.
    assert num_checker (6) == "Fizz"
    assert num_checker (9) == "Fizz"

# testing buzz 

def test_buzz():
    assert num_checker(5) == "Buzz" # using known multiples of 5 to test Buzz element of function
    assert num_checker(10) == "Buzz"

# testing FizzBuzz 
def test_FizzBuzz():
    assert num_checker (15) == "FizzBuzz" #  using known multiples of both 3 and 5 to test Buzz element of function
    assert num_checker (30000) == "FizzBuzz"



