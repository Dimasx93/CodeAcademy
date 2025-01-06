# New Tank game using Turtle library        04/01/2025
from turtle import Screen, Turtle
import random
import time

# Set up the screen
screen = Screen()
screen.title("Tank Game")
screen.bgcolor("lightblue")
screen.setup(width=800, height=600)
screen.tracer(0)  # Disable automatic screen updates for smoother control


# Tank class to manage the tank's movement and actions
class Tank:
    def __init__(self):
        self.bullets = []  # List to store active bullets
        self.tank = Turtle()
        self.tank.shape("turtle")
        self.tank.color("green")
        self.tank.shapesize(stretch_wid=2, stretch_len=2)
        self.tank.penup()
        self.tank.speed(0)
        self.tank.setposition(0, -200)  # Starting position
        self.tank.setheading(90)  # Tank starts facing upwards
        self.direction = 90

    def move_up(self):
        self.tank.sety(self.tank.ycor() + 20)

    def move_down(self):
        self.tank.sety(self.tank.ycor() - 20)

    def move_left(self):
        self.tank.setx(self.tank.xcor() - 20)

    def move_right(self):
        self.tank.setx(self.tank.xcor() + 20)

    def rotate_left(self):
        self.direction -= 15
        self.tank.setheading(self.direction)

    def rotate_right(self):
        self.direction += 15
        self.tank.setheading(self.direction)

    def shoot(self):
        bullet = Bullet(self.tank.xcor(), self.tank.ycor(), self.direction)
        self.bullets.append(bullet)
        bullet.fire()

    def reset(self):
        self.tank.setposition(0, -200)
        self.tank.setheading(90)


# Bullet class to manage the bullets
class Bullet:
    def __init__(self, x, y, direction):
        self.bullet = Turtle()
        self.bullet.shape("circle")
        self.bullet.color("red")
        self.bullet.penup()
        self.bullet.speed(10)
        self.bullet.setposition(x, y)
        self.bullet.setheading(direction)

    def fire(self):
        self.bullet.forward(20)

    def move(self):
        self.bullet.forward(15)


# Target class to manage the target
class Target:
    def __init__(self):
        super().__init__()
        self.target = Turtle()
        self.target.shape("circle")
        self.target.color("blue")
        self.target.penup()
        self.target.speed(0)
        self.target.setposition(0, 100)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-380, 380)
        random_y = random.randint(-280, 280)
        self.target.goto(random_x, random_y)


# Scoreboard class to display score and high score
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("turtle_score.txt") as data:
                content = data.read()
                if content:  # Check if the file contains any content
                    self.high_score = int(content)
                else:
                    self.high_score = 0  # Set to 0 if the file is empty
        except FileNotFoundError:
            self.high_score = 0  # Default high score if the file does not exist

        self.color("yellow")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("turtle_score.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


# Create the objects
tank = Tank()
target = Target()
scoreboard = Scoreboard()

# Keyboard bindings
screen.listen()
screen.onkey(tank.move_up, "Up")
screen.onkey(tank.move_down, "Down")
screen.onkey(tank.move_left, "Left")
screen.onkey(tank.move_right, "Right")
screen.onkey(tank.rotate_left, "a")  # Rotate left (counterclockwise)
screen.onkey(tank.rotate_right, "d")  # Rotate right (clockwise)
screen.onkey(tank.shoot, "space")  # Shoot bullet

# Main game loop
game_is_on = True
last_refresh_time = time.time()

while game_is_on:
    screen.update()  # Manually update the screen
    time.sleep(0.1)  # Control the speed of the game loop

    # Move all active bullets
    for bullet in tank.bullets:
        bullet.move()

        # Remove bullet if it goes off the screen
        if abs(bullet.bullet.xcor()) > 400 or abs(bullet.bullet.ycor()) > 300:
            bullet.bullet.hideturtle()
            tank.bullets.remove(bullet)

    # Check if any bullet hits the target
    for bullet in tank.bullets:
        if target.target.distance(bullet.bullet) < 15:
            target.target.hideturtle()
            target = Target()  # Create a new target after one is hit
            bullet.bullet.hideturtle()  # Hide the bullet after it hits the target
            tank.bullets.remove(bullet)  # Remove bullet from the list
            scoreboard.increase_score()

    # Refresh target every 5 seconds
    time_now = time.time()
    if time_now - last_refresh_time >= 6:
        target.refresh()
        last_refresh_time = time_now

    # Check if the tank goes off the screen
    if abs(tank.tank.xcor()) > 380 or abs(tank.tank.ycor()) > 270:
        user_input = input("Game over, would you like to continue? (Y/N) ")
        if user_input.lower() == "y":
            tank.reset()
            target.refresh()
            scoreboard.reset()
        elif user_input.lower() == "n":
            game_is_on = False  # End the game loop
            screen.bye()  # Close the window
        else:
            print("Enter a valid answer. (Y/N)")

    # Update the screen at the end of the loop
    screen.update()
