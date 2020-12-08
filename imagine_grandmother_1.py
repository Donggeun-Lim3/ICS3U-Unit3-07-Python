#!/usr/bin/env python3

# Created by Donggeun Lim
# Created on December 2020
# This program checks if your age is 25 up and 40 down.

def main():
    # input
    integer_as_string = input("Enter your age : ")
    print("")

    # Process
    try:
        integer_as_number = int(integer_as_string)

        if integer_as_number > 25 and integer_as_number < 40:
            # output
            print("You can date with her grandchild!")
        else:
            print("You can not date with her grandchild.")

    except Exception:
        print("This was not an integer")


if __name__ == "__main__":
    main()
