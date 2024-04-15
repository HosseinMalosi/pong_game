from turtle import Turtle

INIT_POSITIONS = [(-285, 0), (280, 0)]


class Pedal(Turtle):

    def __init__(self, position):
        super().__init__()
        self.pedals = []
        self.shape("square")
        self.shapesize(2.5, 0.5, 1)
        self.color("white")
        self.shape("square")
        self.penup()
        self.speed("slow")
        self.goto(position)
        self.pedals.append(self)

    def up(self):
        """move pedal up"""
        if self.ycor() < 180  :
            self.sety(self.ycor() + 20)

    def down(self):
        """move pedal down"""
        if self.ycor() > -180 :
            self.sety(self.ycor() - 20)
