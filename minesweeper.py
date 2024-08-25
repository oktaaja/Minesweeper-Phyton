import tkinter as tk
import random

class Minesweeper:
    def __init__(self, master, size=10, mines=10):
        self.master = master
        self.size = size
        self.mines = mines
        self.buttons = []
        self.mine_positions = set()
        self.create_widgets()
        self.place_mines()

    def create_widgets(self):
        for i in range(self.size):
            row = []
            for j in range(self.size):
                button = tk.Button(self.master, width=2, height=1, command=lambda i=i, j=j: self.click(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def place_mines(self):
        while len(self.mine_positions) < self.mines:
            i, j = random.randint(0, self.size-1), random.randint(0, self.size-1)
            self.mine_positions.add((i, j))

    def click(self, i, j):
        if (i, j) in self.mine_positions:
            self.buttons[i][j].config(text='*', bg='red')
            self.game_over()
        else:
            mine_count = self.count_mines(i, j)
            self.buttons[i][j].config(text=str(mine_count), state='disabled')
            if mine_count == 0:
                self.reveal_empty(i, j)

    def count_mines(self, i, j):
        count = 0
        for x in range(max(0, i-1), min(self.size, i+2)):
            for y in range(max(0, j-1), min(self.size, j+2)):
                if (x, y) in self.mine_positions:
                    count += 1
        return count

    def reveal_empty(self, i, j):
        for x in range(max(0, i-1), min(self.size, i+2)):
            for y in range(max(0, j-1), min(self.size, j+2)):
                if self.buttons[x][y]['state'] == 'normal':
                    mine_count = self.count_mines(x, y)
                    self.buttons[x][y].config(text=str(mine_count), state='disabled')
                    if mine_count == 0:
                        self.reveal_empty(x, y)

    def game_over(self):
        for i, j in self.mine_positions:
            self.buttons[i][j].config(text='*', bg='red')
        tk.messagebox.showinfo("Game Over", "You hit a mine!")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Minesweeper")
    game = Minesweeper(root)
    root.mainloop()
