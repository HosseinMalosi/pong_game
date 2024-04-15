from turtle import Screen , Turtle
from pedal import Pedal
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(600,400)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# calling pedal classes
l_pedal=Pedal((-285,0))
r_pedal =Pedal((280,0))
ball = Ball()
scoreboard = Scoreboard()

# combining keys
screen.listen()
screen.onkeypress(r_pedal.up,"Up")
screen.onkeypress(r_pedal.down,"Down")
screen.onkeypress(l_pedal.up,"w")
screen.onkeypress(l_pedal.down,"s")

# updating screen after base move
game_is_on= True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # detect collision
    if ball.ycor() > 180 or ball.ycor() < -180:
        ball.w_bounce()
        
    # detect pedal colision
    
    if ball.xcor() > 260  and ball.distance(r_pedal) < 50:
        ball.p_bounce()
    
    if ball.xcor() < -260  and ball.distance(l_pedal) < 50:
        ball.p_bounce()
        
        
    # detect misses 
    
    if ball.xcor() > 300 : 
        ball.reset_position()
        scoreboard.score_l +=1
        
    if ball.xcor( ) < -300 :
        ball.reset_position()
        scoreboard.score_r +=1
        
    scoreboard.update_score()   
    # scoreboard 
        
        
    

















screen.exitonclick()