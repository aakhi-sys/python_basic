# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 17:50:32 2024

@author: rumana
"""

def valid_positive_integer():  # Method to handle input validation
    while True:
        user_input = input("Enter a positive integer: ")
        try:
            number = int(user_input)
            if number > 0:
                return number
            else:
                print("Invalid input. Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def prime_factors_find(number):  # Method to determine the prime factors of a given number.
    prime_factors = []
    
    while number % 2 == 0:     # Repeatedly divide the number by 2 until it is no longer even.
        prime_factors.append(2)
        number //= 2
 
    factor = 3     # Look for odd factors beginning at 3 and extending to the square root of the number.
    while factor * factor <= number:
        while number % factor == 0:
            prime_factors.append(factor)
            number //= factor
        factor += 2
    
    if number > 2:    # Verify if the number is a prime number and above 2.
        prime_factors.append(number)
    
    return prime_factors

def P_F_F():     # Main program start here
    print("Welcome to the Prime Factor Finder!")
    
    while True:
        number = valid_positive_integer()  # Get validated user input
        
        prime_factors = prime_factors_find(number)
        print(f"Prime factors of {number} are: {' '.join(map(str, prime_factors))}")
        
        # Ask if the user wants to continue or exit
        choice = input("Do you want to find prime factors for another number? (yes/no): ").lower()
        if choice != 'yes':
            print("Thank you for using Prime Factor Finder!")
            break

P_F_F() # Start the program Prime Factor Finder