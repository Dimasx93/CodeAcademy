# tank_game.py
import random
import csv


class TankGame:
    def __init__(self, N: int = 7):
        """Create a tank game object.

        :param N: the size of the map (grid) NxN to generate for the game.
        """
        self.N = N
        # Hard-coded starting tank location is 2, 1
        self.tank_loc_x = 2
        self.tank_loc_y = 1
        # Starting direction: tank facing north/up
        self.direction = "up"
        self.number_of_shots = 0
        self.direction_of_shots = {"left": 0, "right": 0, "up": 0, "down": 0}
        self.target_x = random.randint(0, 6)
        self.target_y = random.randint(0, 6)
        self.tot_points = 100
        self.target_hit = 0

    def print_map(self):
        """Print the current map of the game.

        Example output for a 7x7 map:
           0  1  2  3  4  5  6
        0  .  .  .  .  .  .  .
        1  .  .  T  .  .  .  .
        2  .  .  .  .  .  .  .
        3  .  .  .  .  .  .  .
        4  .  .  .  .  .  .  .
        5  .  .  .  .  .  .  .
        6  .  .  .  .  .  .  .

        where T is the location of the tank,
        where . (the dot) is an empty space on the map,
        where the horizontal axis is the x location of the tank and,
        where the vertical axis is the y location of the tank.
        """
        # Print the numbers for the x axis
        print("   " + "  ".join([str(i) for i in range(self.N)]))

        for i in range(self.N):
            # Print the numbers for the y axis
            print(f"{i} ", end="")
            for j in range(self.N):
                if self.tank_loc_x == j and self.tank_loc_y == i:
                    print(" T ", end="")  # Tank position
                elif self.target_x == j and self.target_y == i:
                    print(" V ", end="")  # Target position
                else:
                    print(" . ", end="")  # Empty space
            print()

    def steer_left(self):
        # TODO implement this
        if self.direction == "up":
            self.direction = "left"
        elif self.direction == "left":
            self.direction = "down"
        elif self.direction == "down":
            self.direction = "right"
        elif self.direction == "right":
            self.direction = "up"

    def steer_right(self):
        # TODO implement this
        if self.direction == "up":
            self.direction = "right"
        elif self.direction == "left":
            self.direction = "up"
        elif self.direction == "down":
            self.direction = "left"
        elif self.direction == "right":
            self.direction = "down"

    def forward(self):
        # TODO implement this
        if self.direction == "up":
            self.tank_loc_y -= 1
        elif self.direction == "left":
            self.tank_loc_x -= 1
        elif self.direction == "down":
            self.tank_loc_y += 1
        elif self.direction == "right":
            self.tank_loc_x += 1
        self.tot_points -= 10

    def backward(self):
        # TODO implement this
        if self.direction == "up":
            self.tank_loc_y += 1
        elif self.direction == "left":
            self.tank_loc_x += 1
        elif self.direction == "down":
            self.tank_loc_y -= 1
        elif self.direction == "right":
            self.tank_loc_x -= 1
        self.tot_points -= 10

    def shoot(self):
        """Fire the tank's weapon."""
        self.number_of_shots += 1
        self.direction_of_shots[self.direction] += 1
        print("SHOT FIRED!")

        # Check if the target is hit in the current direction
        if self.direction == "up" and self.target_x == self.tank_loc_x and self.target_y < self.tank_loc_y:
            print("YOU HIT THE TARGET!")
            self.tot_points += 30
            self.target_hit += 1
            self.reset_target()  # Reset the target to a new random position
        elif self.direction == "down" and self.target_x == self.tank_loc_x and self.target_y > self.tank_loc_y:
            print("YOU HIT THE TARGET!")
            self.tot_points += 30
            self.target_hit += 1
            self.reset_target()  # Reset the target to a new random position
        elif self.direction == "left" and self.target_y == self.tank_loc_y and self.target_x < self.tank_loc_x:
            print("YOU HIT THE TARGET!")
            self.tot_points += 30
            self.target_hit += 1
            self.reset_target()  # Reset the target to a new random position
        elif self.direction == "right" and self.target_y == self.tank_loc_y and self.target_x > self.tank_loc_x:
            print("YOU HIT THE TARGET!")
            self.tot_points += 30
            self.target_hit += 1
            self.reset_target()  # Reset the target to a new random position
        else:
            print("YOU MISSED!")

    def reset_target(self):
        """Reset the target to a new random position, ensuring it's not at the tank's position."""
        while True:
            self.target_x = random.randint(0, 6)
            self.target_y = random.randint(0, 6)
            if self.target_x != self.tank_loc_x or self.target_y != self.tank_loc_y:
                break  # Exit the loop when a valid target position is found

    def info(self):
        print(f"Direction: {self.direction}")
        print(f"Position: {(self.tank_loc_x, self.tank_loc_y)}")
        print(f"Target location: {(self.target_x, self.target_y)}")
        print(f"Number of shots: {self.number_of_shots}")
        print(f"Direction of shots: {self.direction_of_shots}")
        print(f"Points: {self.tot_points}")

    def target(self):
        """Print the map with only the target location."""
        # Print the numbers for the x axis
        print("   " + "  ".join([str(i) for i in range(self.N)]))

        for i in range(self.N):
            # Print the numbers for the y axis
            print(f"{i} ", end="")
            for j in range(self.N):
                if self.target_x == j and self.target_y == i:
                    print(" V ", end="")  # Target position
                else:
                    print(" . ", end="")  # Empty space
            print()

    def make_chart(self):
        name = input("Please enter your name: ")
        with open("tank.csv", "a", newline='') as f:
            if f.tell() == 0:  # If file is empty, write header
                f.write("name, points, targets hit\n")
            f.write(f"{name}, {self.tot_points}, {self.target_hit}\n")

    def view_chart(self):
        # Read the file and print the player stats
        try:
            with open("tank.csv", "r") as f:
                reader = csv.reader(f)
                next(reader)  # Skip the header row
                print("\n--- Player Stats ---")
                print(f"{'Name':<15}{'Points':<10}{'Targets Hit'}")
                print("-" * 40)

                # Print each player's data from the file
                for row in reader:
                    name, points, targets_hit = row
                    print(f"{name:<15}{points:<10}{targets_hit}")
        except FileNotFoundError:
            print("No chart data found. Please make sure the game has saved some results first.")

    def end_game(self):
        print(f"Total targets hit: {self.target_hit}")
        print(f"Number of shots: {self.number_of_shots}")
        print(f"Direction of shots: {self.direction_of_shots}")


if __name__ == "__main__":
    # Initialize your game object
    tg = TankGame()

    # Start game loop
    game_on = True
    while game_on:
        tg.print_map()

        # Debug print to track points
        print(f"Current Points: {tg.tot_points}")

        # Check if the game should end due to zero points
        if tg.tot_points <= 0:
            tg.end_game()
            game_on = False
            break  # End the loop if the game is over

        # Get user input for the next action
        command = input("Input a command: ").lower()

        # Handle the various commands
        if command == "left":
            tg.steer_left()
        elif command == "right":
            tg.steer_right()
        elif command == "forward":
            tg.forward()
            print(f"Points after moving forward: {tg.tot_points}")  # Debug print for forward action
        elif command == "backward":
            tg.backward()
            print(f"Points after moving backward: {tg.tot_points}")  # Debug print for backward action
        elif command == "shoot":
            tg.shoot()
            print(f"Points after shooting: {tg.tot_points}")  # Debug print for shoot action
        elif command == "info":
            tg.info()

        elif command == "exit":
            tg.make_chart()
            tg.view_chart()
            break
        elif command == "top":
            tg.view_chart()

        # Check again after every action in case points hit 0 mid-action
        if tg.tot_points <= 0:
            tg.end_game()
            game_on = False
            break
