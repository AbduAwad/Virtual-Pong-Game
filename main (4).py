from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

width = 600
height = 400
screen = Screen()
screen.bgcolor("black")
screen.setup(width, height)
screen.title("Pong Game")
screen.tracer(0)

ball = Ball()
scoreboard = Scoreboard()
right_paddle = Paddle((250, 0))
left_paddle = Paddle((-250, 0))

#Move paddle up and down, Wont Go up or down go back over

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

game_on = True
while game_on:
  
  time.sleep(ball.sleep_time) # 0.005 second pause between each iteration of the loop
  screen.update()
  ball.move()

  #Detect if ball collided with ceiling or floor of screen
  if ball.ycor() > 180 or ball.ycor() < -180:
    ball.move_opposite_y()
    
  #Detect if ball collided with walls of screen
  if ball.xcor() > 280 or ball.xcor() < -280:
    ball.move_opposite_x()

  #Detect collision with right and left paddle
  if ball.distance(right_paddle) < 70 and ball.xcor() == 240 or ball.distance(left_paddle) < 50 and ball.xcor() == -240:
    ball.move_opposite_x()
    
  #Detect if right paddle misses ball
  if ball.xcor() > 240:
    ball.reset_pos()
    scoreboard.right_point()
    
  #Detect if Left paddle misses ball
  if ball.xcor() < -240:
    ball.reset_pos()
    scoreboard.left_point()
#screen.exitonclick()