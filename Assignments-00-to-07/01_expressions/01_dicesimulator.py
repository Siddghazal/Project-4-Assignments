import random

NUM_SIDES = 6

def roll_dice():
    
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    print(f"Die 1: {die1}, Die 2: {die2}")
    
    total: int = die1 + die2
    print("Total of two dice:", total)

def main():
    die1: int = 10
    print(f"die1 in main() start as {die1}")
    
    for _ in range(3):
     roll_dice()

     print(f"\ndie1 in main() is still {die1}")  


if __name__ == '__main__':
    main()