#!/usr/bin/env python3
# Created by: Nathan Araujo
# Created on: Oct 28 2022
# This program determines the factorial of the users number


def main():
    # set counter and product to 1
    product = 1
    counter = 0
    # Get the users number
    user_num_string = input("Enter a integer: ")

    # An try catch to catch any errors if they enter a string or a decimal
    try:
        user_num = int(user_num_string)
    except Exception:
        print("Please a enter valid integer")
    else:
        # An if statement to see if the integer is a negative
        if user_num >= 0:
            # A do while loop to calculate the factorial of the users num
            while True:
                counter = counter + 1
                product *= counter
                if counter >= user_num:
                    break
            print("The factorial of {}".format(user_num), "= {}".format(product))
        else:
            print("Please enter a positive integer")


if __name__ == "__main__":
    main()
