from turtle import Turtle

class Ball(Turtle): #Super class: turtle class available in Ball class
  def __init__(self):
    super().__init__()
    
    self.shape("circle")
    self.penup()
    self.color("white")
    self.x_move = 10
    self.y_move = 10
    self.sleep_time = 0.1
    
  def move(self):
    new_x = self.xcor() + self.x_move
    new_y = self.ycor() + self.y_move
    self.goto(new_x, new_y)

  def move_opposite_y(self):  
    self.y_move *= -1

  def move_opposite_x(self):  
    self.x_move *= -1
    self.sleep_time *= 0.75

  def reset_pos(self):
    self.goto(0,0)
    self.sleep_time = 0.1
    self.move_opposite_x()
