from .lake import draw_lake
from .park import draw_park
from .gazebo import draw_gazebo

def draw_outdoors():
    draw_lake()
    draw_park()
    draw_gazebo()
    return
