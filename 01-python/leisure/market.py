import numpy as np
def draw_market():
    chance_of_disaster = 0.05
    today = np.random.random()
    if today > chance_of_disaster:
        items = ['Carrots', 'Tomatoes', 'Ointments', 'Juices', 'Bananas', 'Onions', 'Trading Cards', 'ALL ITEMS']
        discounts = ['5%', '10%', '20%', '30%', '40%']
        item = np.random.choice(items)
        discount = np.random.choice(discounts)
        print(f"{item} are {discount} off in the Market today!")
    else:
        print("THE MARKET IS ON FIRE!")
    return
