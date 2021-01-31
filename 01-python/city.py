from safety.safety import draw_safety
from leisure.leisure import draw_leisure
from outdoors.outdoors import draw_outdoors
from education.education import draw_education
from infrastructure.infrastructure import draw_infrastructure

def draw_city():
    draw_safety()
    draw_infrastructure()
    draw_leisure()
    draw_outdoors()
    draw_education()
    return

draw_city()
