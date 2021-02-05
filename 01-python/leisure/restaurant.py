import random
def draw_restaurant():
    appetizers = ['chips and salsa', 'tomato soup', 'chicken wings']
    maincourses = ['garden salad', 'steak and potatoes', 'spaghetti and meatballs']
    desserts = ['ice cream', 'chocolate cake', 'blueberry cheesecake']
    drinks = ['coke', 'pepsi', 'sprite']
    print("Your appetizer is " + random.choice(appetizers)+ "!")
    print("Your main course is " + random.choice(maincourses)+ "!")
    print("Your dessert is " + random.choice(desserts) + "!")
    print("Your drink is " + random.choice(drinks) + "!")
    return