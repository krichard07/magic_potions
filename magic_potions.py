print("Welcome to the Magic Potion Shop!\nHere are the potions we offer:")

potions = {"Invisibility Potion": ["Moonstone", "Dragon scale", "Fairy dust"], 
           "Flying Potion": ["Phoenix feather", "Troll tooth", "Mermaid scale"], 
           "Healing Potion": ["Unicorn horn", "Elf hair", "Golden apple"]}

for potion in potions:
    print(potion)

choose = input("Wich potion would you like to buy ingredients for? ").title().strip()
print()

if choose in potions:
    print(f"The ingredients of {choose} are:")
    for ingredient in potions[choose]:
        print(ingredient)
    print()

    print("Let's start buying the ingredients!")

    while potions[choose]:
        ingredient = potions[choose].pop(0)
        buy_ingredient = input(f"Do you want to buy {ingredient}? (yes/no) ")
        
        if buy_ingredient == "yes":
            print(f"You bought {ingredient}!")
        else:
            print("You chose to stop shopping.")
            break

    if not potions[choose] and buy_ingredient == "yes":
        print(f"Congratulations! You bought all ingredients for {choose}.")
else:
    print("Sorry, we do not have this potion!")