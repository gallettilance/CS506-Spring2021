from .power import draw_power_plant
from .road import draw_road
from .tree import draw_tree

def draw_infrastructure():
    draw_tree()
    draw_road()
    draw_power_plant()
    return