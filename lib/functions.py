#!/usr/bin/env python3

def greet_programmer():
    print ("Hello, programmer!")
    pass

def greet(name):
    print (f"Hello, {name}!")
    pass

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
    pass

def add(num1, num2):
    return num1 + num2
    pass

def halve(number):
    if isinstance(number, (int, float)):
        return number / 2
    else:
        return None
    pass
