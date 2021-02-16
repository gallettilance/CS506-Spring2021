import random
def draw_restaurant():
    menu_items = ['margarita pizza', 'pesto pasta', 'spaghetti and meatballs', 'lasagne', 'burrata']
    print("[-----This is an Italian Restaurant.-----]")
    print("The special of the day is " +random.choice(menu_items))
    return
