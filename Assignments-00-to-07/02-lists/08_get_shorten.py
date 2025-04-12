MAX_LENGTH: int = 3

# Rangon ke liye ANSI codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()
        print(RED + "Removed:" + RESET, last_elem)

def get_lst():
    lst = []
    elem = input(YELLOW + "List ka item likho (ya enter dabao rukne ke liye): " + RESET)
    while elem != "":
        lst.append(elem)
        elem = input(YELLOW + "Next item (ya enter dabao rukne ke liye): " + RESET)
    return lst

def main():
    lst = get_lst()
    print(GREEN + "Pehle wali list:" + RESET, lst)
    shorten(lst)
    print(GREEN + "Bach gayi list:" + RESET, lst)

if __name__ == '__main__':
    main()
