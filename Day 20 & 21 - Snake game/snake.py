from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    # Angela's take on creating snake's body:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.penup()
        new_segment.color('white')
        new_segment.goto(position)
        self.body.append(new_segment)

    def extend(self):
        self.add_segment(self.body[-1].position())


    # Letting snake move forward by moving last piece of snake's body part in place one before last snake's body part
    def move(self):
        for seg_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[seg_num - 1].xcor()
            new_y = self.body[seg_num - 1].ycor()
            self.body[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def resett(self):
        for seg in self.body:
            seg.reset()
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]

# My take on creating snake's body (also works):
# snake_length = 3
# x_starting_position = 0
# for starting_body_part in range(snake_length):
#     square = Turtle('square')
#     square.color('white')
#     square.penup()
#     square.goto(x_starting_position, 0)
#     x_starting_position -= 20
#     body.append(square)
