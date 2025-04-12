def main():
    # Ask the user for a number
    curr_value = int(input("Enter a number: "))

    # Double the number until it reaches 100 or more
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
