from turtle import Turtle
pos = () # tupple
class Paddle(Turtle):
  def __init__(self, pos):
    super().__init__()
    self.shape("square")
    self.shapesize(5, 1) #Stretches out width and heigh by x5 and x1
    self.color("white")
    self.penup()
    self.goto((pos))

  def move_up(self):
    new_y = self.ycor() + 50
    self.goto(self.xcor(), new_y)
  
  def move_down(self):
    new_y = self.ycor() - 50
    self.goto(self.xcor(), new_y)