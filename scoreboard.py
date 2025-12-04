from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.teleport(0, 270)
        self.hideturtle()
        self.show_score()

    def show_score(self):
        """Clears the previous text and display the current score on the screen."""
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increases the score by 1."""
        self.score += 1
        self.show_score()

    def show_game_over(self):
        """Displays the message "GAME OVER" in the center of the screen."""
        self.teleport(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)