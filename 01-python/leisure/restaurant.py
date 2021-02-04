import random

def randomSpecial():
    special = ["Lobster Spaghetti", "Beef Wellington", "Peking Duck", "Sukiyaki", "Sichuan Hotpot", "Big Mac"]
    return random.choice(special)

def draw_restaurant():
    print("This is an All-you-can-eat restaurant providing all kinds of tasty food. Free for BU members!")
    print("daily menu: Error: the file is too big, DATA OVERFLOW!")
    print("Though the menu explodes due to technique problems out of kitchen, our Chief still remembers to offer today's special.")
    ts = randomSpecial()
    print("Today's special is: "+ ts + ". CHEERS!")
    return