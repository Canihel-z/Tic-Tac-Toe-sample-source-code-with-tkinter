import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master, ):
        self.master = master
        master.title("Tic Tac Toe")

        self.current_player = "X"
        self.board = [None] * 9  # Représente les 9 cases du tableau
        self.buttons = []

        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(master, text="", width=5, height=2, font=("Arial", 24),
                                   command=lambda i=i, j=j: self.make_move(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def make_move(self, i, j):
        index = i * 3 + j
        if self.board[index] is None:
            self.board[index] = self.current_player
            self.buttons[i][j].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Félicitations!", f"Le joueur {self.current_player} a gagné !")
                self.reset_game()
            elif None not in self.board:
                messagebox.showinfo("Match nul", "C'est un match nul !")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Combinaisons gagnantes
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Lignes
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Colonnes
            (0, 4, 8), (2, 4, 6)              # Diagonales
        ]
        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] is not None):
                return True
        return False

    def reset_game(self):
        self.board = [None] * 9
        self.current_player = "X"
        for row in self.buttons:
            for button in row:
                button.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
