from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.color("green")
        self.go_to_start()

    def go_to_start(self):
        """ Sets the starting position of the turtle"""
        self.goto(STARTING_POSITION)

    def go_up(self):
        """ Moves the turtle object upwards based on the MOVE_DISTANCE"""
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def is_at_finish_line(self):
        """ Detects if the turtle object is at the finish line"""
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
