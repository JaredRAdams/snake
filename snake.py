"""
This module implements the snake class.
"""

from gui import Gui
from position import Position
from typing import List
opposites = {"UP":"DOWN","DOWN":"UP","RIGHT":"LEFT","LEFT":"RIGHT"}
class Snake:
    """This is the Snake.

    It has a list of positions. The head is at index 0.
    The tail occupies the rest of the list.
    """


    def __init__(self):
        self.direction = "RIGHT"
        self.headPosition = [60,15]
        self.bodyPosition = [[59,15],[58,15]]

    def change_direction(self, direction):
        if direction != opposites[self.direction] :
            self.direction = direction
        else:
            return

    def draw(self, gui):
        directon_map = {"UP":"^","RIGHT":">","LEFT":"<","DOWN":"V"}
        head = directon_map[self.direction]
        gui.draw_text(head,self.headPosition[0],self.headPosition[1],"BLACK","WHITE")
        for i in range (0,len(self.bodyPosition)):
            gui.draw_text("+",self.bodyPosition[i][0],self.bodyPosition[i][1],"BLACK","WHITE")

    def move(self):
        for i in range(len(self.bodyPosition)-1, 0 , -1):
            self.bodyPosition[i] = self.bodyPosition[i-1][:]
        self.bodyPosition[0] = self.headPosition[:]

        if self.direction == "RIGHT":
            self.headPosition[0] += 1
        if self.direction == "DOWN":
            self.headPosition[1] += 1
        if self.direction == "LEFT":
            self.headPosition[0] -= 1
        if self.direction == "UP":
            self.headPosition[1] -= 1
