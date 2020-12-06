"""
This module represents the apple that appears at random places on the screen.
"""
import random
from typing import List

from gui import Gui
from position import Position
from snake import Snake
gui = Gui()
snake = Snake()

def collides(p, positions):
    """Return true if p is any of the positions in the list."""
    for position in positions:
        if p.get_x() == position.get_x() and p.get_y == position.get_y():
            return True
    return False


class Apple:
    """The apple's location is randomly generated."""

    def __init__(self):
        self.x = random.randint(1,119)
        self.y = random.randint(1,29)
        while self.x == snake.headPosition[0] and self.y == snake.headPosition[1]:
            self.x = random.randint(1,119)
            self.y = random.randint(1,29)




    def draw(self, gui):
        gui.draw_text("*",self.x,self.y,"RED","GREEN")
