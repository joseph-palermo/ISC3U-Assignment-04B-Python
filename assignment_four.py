#!/usr/bin/env python3

# Created by: Joseph Palermo
# Created on: October 2019
# This program calculates if value a is greater than value b


def main():
    # This function calculates if value a is greater than value b

    # input
    a_string = input("Enter value a: ")
    b_string = input("Enter value b: ")

    # process and output
    try:
        a_int = float(a_string)
        b_int = float(b_string)

        if (a_int > b_int):
            print("")
            print("Value a > value b")
        elif (a_int == b_int):
            print("")
            print("Value a = value b")
        elif (b_int > a_int):
            print("")
            print("Value b > value a")
        else:
            print("")
            print("Please put in numerical values.")
    except ValueError:
        print("")
        print("Please put in numerical values.")


if __name__ == "__main__":
    main()
