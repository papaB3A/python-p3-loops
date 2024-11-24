#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i= 10
    while i>= 1:
        print(i)
        if(i== 1):
            print("Happy New Year!")
        i-=1
    pass

def square_integers(int_list):
    # code goes here!
    int_list= [integer*integer for integer in int_list]
    print(int_list)
    pass

def fizzbuzz():
    # code goes here!
    for number in range(1, 101):
        if (number%3== 0) and (number%5== 0):
            print("FizzBuzz")
        elif number%3== 0:
            print("Fizz")
        elif number%5== 0:
            print("Buzz")
        else:
            print(number)
    pass

# happy_new_year()
# square_integers([1, 2, 3, 4, 5])
fizzbuzz()
