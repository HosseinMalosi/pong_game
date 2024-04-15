from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.8, 0.8, 1)
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed=0.1
        
    def move(self):
        new_y=self.ycor() + self.y_move
        new_X=self.xcor() + self.x_move
        self.goto(new_X, new_y)

    def w_bounce(self):
        """ reverse y moving"""
        self.y_move *= -1
    
    def p_bounce(self):
        """ reverse x moving"""
        self.x_move *= -1 
        self.move_speed *= 0.9  
        
    def reset_position(self):
        self.goto(0, 0)
        self.p_bounce()
        self.move_speed = 0.1