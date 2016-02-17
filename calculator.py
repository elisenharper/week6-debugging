#Elise Harper Calculator#

def add( first, second):
    # TODO:
    # there's an error in this code, fix it
    return first + second  #Added a + sign instead of the word plus

def subtract( first, second):
    # TODO:
    # fill in code here that will return the difference between first and second
    return first - second   #Added this line that will subtract the two numbers

def multiply( first, second):
    # TODO:
    # fill in code here that will return the product of first and second
    return first * second  #Added this line that will multiply the two numbers

def divide( first, second):
    # TODO:
    # fill in code here that:
    #   1. checks the second number to see if it is zero
    #   2. if the second number is zero, an exception is raised, the exception text must say exactly the following (make sure everything including casing and spaces match)
    #       I'm sorry, I can't divide by zero
    #   3. returns the quotient of first and second

    if second == 0:
        raise Exception ("I'm sorry, I can't divide by zero")  #If the second number is zero then the exception will be raised
    return first / second #Added this line that will divide the two numbers
