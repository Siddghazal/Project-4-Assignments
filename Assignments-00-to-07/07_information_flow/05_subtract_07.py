def main():
    num = int(input("Enter a number: "))       # Taking input from the user
    num = subtract_seven(num)                  # Subtracting 7 from the input
    print("After subtracting 7:", num)         # Printing the result

def subtract_seven(num):
    return num - 7                             # Return the number after subtracting 7

if __name__ == '__main__':
    main()
