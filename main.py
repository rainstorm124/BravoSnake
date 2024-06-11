import tkinter as tk
import random

GAME_ON = False
BODY_SIZE = 2
GRID_SQUARE = 10
SNAKE_COLOR = "#64FF33"
FOOD_COLOR = "#3377FF"
ENEMY_SNAKE_COLOR = "#BD2D1C"
PREY_COLOR = "#AFCB22"

"""
Entities include:
- The Snake
- Food (Randomly appears, increments snake size by 1)
- Enemy Snake (Randomly appears, moves half as fast as snake, paths towards end of snake)
- Prey (Randomly appears, moves towards food, if caught increments snake size by 1,
if caught after eating food, increments snake size by 2
starts randomly at one of the edges, moves towards food at snake speed
until fed or eaten - then, once fed, waits 5 seconds then attempts to flees to its original "Burrow")
"""

class Snake:
    def __init__(self):
        self.bodysize = BODY_SIZE
        self.coordinates = []
        self.squares = []

        for i in range(self.bodysize):
            self.coordinates.append([0,0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x+GRID_SQUARE, y+GRID_SQUARE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0, int((500/GRID_SQUARE)-1)) * GRID_SQUARE
        y = random.randint(0, int((500/GRID_SQUARE)-1)) * GRID_SQUARE
        self.coordinates = [x,y]

        canvas.create_oval(x, y, x+GRID_SQUARE, y+GRID_SQUARE, fill=FOOD_COLOR, tag="food")

def startgame():
    GAME_ON = True

root = tk.Tk()
root.title("Rain's Snake Game")
root.geometry("500x500")
root.mainloop()

readyPlayer = tk.Label(root, text="Hello! This is my snake game. Are you ready to play?")
readyPlayer.place(anchor='center')
readyPlayer.grid(row=0, column=0)
startButton = tk.Button(root, text="START", width=20, height=20, command=startgame)
canvas = tk.Canvas(root, bg="white", width=500, height=500)
snake = Snake()
food = Food()
