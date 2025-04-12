def main():
    fruits = {'apple': 2.5, 'durian': 50, 'jackfruit': 50, 'kiwi': 4, 'rambutan': 2.5, 'mango': 8}
    
    total_cost = 0
    for fruit_name in fruits:
        price = fruits[fruit_name]
        amount_bought = int(input("\033[94mHow many (" + fruit_name + ") do you want to buy?:\033[0m "))
        total_cost += (price * amount_bought)
    
    print("Your total is $" + str(total_cost))


if __name__ == '__main__':
    main()