from turtle import Turtle
ALIGNMENT = "center"
FRONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 250)
        self.color("white")
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FRONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over!", align=ALIGNMENT, font=FRONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()

