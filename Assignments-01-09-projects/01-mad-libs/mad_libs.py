def mad_libs():
    print("Welcome to Mad Libs! Fill in the blanks below:\n")

    # User Inputs
    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb (past tense): ")
    adverb = input("Enter an adverb: ")
    adjective2 = input("Enter another adjective: ")
    noun2 = input("Enter another noun: ")
    noun3 = input("Enter one more noun: ")
    verb2 = input("Enter another verb (past tense): ")
    adjective3 = input("Enter one more adjective: ")

    # Story Template
    story = f"""
    Today I went to the zoo. I saw a(n) {adjective1} {noun1} jumping up and down in its tree.
    It {verb1} {adverb} through the large tunnel that led to its {adjective2} {noun2}.
    I got some peanuts and passed them through the cage to a gigantic {noun3}
    that {verb2} just like a {adjective3} monkey!
    """

    print("\nHere's your Mad Libs story:\n")
    print(story)

# Run the game
mad_libs()
