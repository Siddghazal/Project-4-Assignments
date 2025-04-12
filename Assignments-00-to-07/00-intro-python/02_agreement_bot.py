def main():
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    RESET = '\033[0m'

    print("Favorite animal!")

    favorite_animal = input(f"{BOLD}{ITALIC}What is your favorite animal___?{RESET} ")

    print(f"My favorite animal is also {favorite_animal}! :)")

if __name__ == '__main__':
    main()
