from .museum import draw_museum
from .restaurant import draw_restaurant
from .mall import draw_mall
from .market import draw_market
from .gym import draw_gym

def draw_leisure():
    draw_museum()
    draw_restaurant()
    draw_mall()
    draw_gym()
    draw_market()
    return