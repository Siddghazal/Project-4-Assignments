def main():
    # Anton's age is given as 21 years old
    anton : int = 21 

     # Beth is 6 years older than Anton, so add 6 to Anton's age to get Beth's
    beth : int = 6 + anton  

      # Chen is 20 years older than Beth, so add 20 to Beth's age to get Chen's
    chen : int = 20 + beth

    # Drew is as old as Chen's age plus Anton's age, so add them together
    drew  : int= chen + anton 

    # Ethan is the same age as Chen, so set Ethan's age equal to Chen's
    ethan : int = chen  

   # Print out all of the ages!
    print(f"Anton is {anton} years old")
    print(f"Beth is {beth} years old")
    print(f"Chen is {chen} years old")
    print(f"Drew is {drew} years old")
    print(f"Ethan is {ethan} years old")


if __name__ == '__main__':
    main()