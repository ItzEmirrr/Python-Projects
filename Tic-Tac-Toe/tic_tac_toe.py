import pygame
import sys

from tictactoe_settings import Settings


class TicTacToe:
    def __init__(self):
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.init()

        pygame.display.set_caption("Tic-Tac-Toe")

        self.board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

    def draw_board(self):
        for i in range(1, 3):
            pygame.draw.line(self.screen, self.settings.line_color, (0, i * 300), (900, i * 300), 2)
            pygame.draw.line(self.screen, self.settings.line_color, (i * 300, 0), (i * 300, 900), 2)

    def draw_X(self, row, col):
        pygame.draw.line(self.screen, self.settings.x_color, (col * 300 + 30, row * 300 + 30), (col * 300 + 270, row * 300 + 270), 2)
        pygame.draw.line(self.screen, self.settings.x_color, (col * 300 + 270, row * 300 + 30), (col * 300 + 30, row * 300 + 270), 2)


    def draw_O(self, row, col):
        pygame.draw.circle(self.screen, self.settings.o_color, (col * 300 + 150, row * 300 + 150), 120, 2)

    def check_for_winner(self):
        winner = None
        for i in range(3):
            if all(self.board[i][j] == "X" for j in range(3)):
                winner = "X"

            elif all(self.board[i][j] == "O" for j in range(3)):
                winner = "O"

            elif all(self.board[j][i] == "X" for j in range(3)):
                winner = "X"

            elif all(self.board[j][i] == "O" for j in range(3)):
                winner = "O"

        if all(self.board[i][i] == "X" for i in range(3)):
            winner = "X"

        elif all(self.board[i][i] == "O" for i in range(3)):
            winner = "O"

        elif all(self.board[i][2 - i] == "X" for i in range(3)):
            winner = "X"

        elif all(self.board[i][2 - i] == "O" for i in range(3)):
            winner = "O"

        return winner

    def run_game(self):
        global board
        turn = "X"
        running = True
        self.draw_board()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()

                    row = y // 300
                    col = x // 300
                    print(row, col)

                    if self.board[row][col] == "":
                        self.board[row][col] = turn

                        if turn == "X":
                            self.draw_X(row, col)
                            turn = "O"
                        elif turn == "O":
                            self.draw_O(row, col)
                            turn = "X"

                    if self.check_for_winner() != None:
                        sys.exit()

            pygame.display.update()

        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    tictactoe = TicTacToe()
    tictactoe.run_game()
