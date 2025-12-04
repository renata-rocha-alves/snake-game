from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.x_position = 0
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates the initial snake's body by adding segments to the segment list."""
        for _ in range(3):
            self.add_segment((self.x_position, 0))
            self.x_position -= MOVE_DISTANCE

    def add_segment(self, position: tuple[float, float]):
        """Adds a segment to the snake's body at the specified position."""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.speed("slowest")
        new_segment.penup()

        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Adds a segment to the snake's body at the end of its current tail."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """
        Moves the segments of the snake in the specified direction. Each segment
        follows the position of the one in front of it, starting from the end, while the head of the
        snake moves forward.
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # Get the position of the segment in front of the current one (previous in the list)
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Moves the snake's head up if it isn't already facing down, so it won't go backwards."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Moves the snake's head down if it isn't already facing up, so it won't go backwards."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        """Moves the snake's head right if it isn't already facing left, so it won't go backwards."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        """Moves the snake's head left if it isn't already facing right, so it won't go backwards."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
