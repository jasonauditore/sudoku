from tkinter import messagebox
import tkinter as tk


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + "", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)

    return None


def is_valid(bo, num, pos):
    #Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    #Check column
    for j in range(len(bo)):
        if bo[j][pos[1]] == num and pos[0] != j:
            return False

    #Check box

    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(bo, i, (row, col)):
            bo[row][col] = i
            if solve(bo):
                return True
            bo[row][col] = 0
    return False


class GUI:
    def __init__(self, root):
        self.root = root
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.root.title("Sudoku Solver")
        self.create_grid()
        self.board = [[0 for _ in range(9)] for _ in range(9)]

    #Creates a grid with 81 empty boxes
    def create_grid(self):
        for i in range(9):
            for j in range(9):
                entry = tk.Entry(self.root, width=3, font="Arial", justify="center")
                entry.grid(row=i, column=j, padx=5, pady=5)
                self.cells[i][j] = entry
        solve_button = tk.Button(self.root, text="Solve", command=self.solve_puzzle)
        solve_button.grid(row=9, column=0, columnspan=9, pady=20)

    #Solves the puzzle using the backtracking algorithm
    def solve_puzzle(self):
        for i in range(9):
            for j in range(9):
                value = self.cells[i][j].get()
                if value.isdigit():
                    self.board[i][j] = int(value)
                else:
                    self.board[i][j] = 0
        if solve(self.board):
            self.update_grid()
        else:
            messagebox.showerror("Error. No  solution for this puzzle ")

    #Updates the grid with the values solved
    def update_grid(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, tk.END)
                self.cells[i][j].insert(0, str(self.board[i][j]))


def main():
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
