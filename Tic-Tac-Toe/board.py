
    def __init__(self, tictactoe_game):
        self.screen = tictactoe_game.screen
        self.settings = tictactoe_game.settings

    def draw_board(self,):
        for i in range(1, 3):
            pygame.draw.line(self.screen, self.settings.line_color, (90, i * 260), (710, i * 260), 2)
            pygame.draw.line(self.screen, self.settings.line_color, (i * 260, 710), (i * 260, 90), 2)


    def draw_x(self, row, coloumn):
        pygame.draw.line(self.screen, self.settings.x_color, (coloumn * 260 + 10, row * 260 + 10), (coloumn * 260 + 90, row * 260 + 90), 2)
        pygame.draw.line(self.screen, self.settings.x_color, (coloumn * 260 + 90, row * 260 + 10), (coloumn * 260 + 10, row * 260 + 90), 2)

    def draw_O(self, row, coloumn):
        pygame.draw.circle(self.screen, self.settings.o_color, (coloumn * 260 + 130, row * 260 + 130), 40, 2)

    def check_for_winner(self):
        winner = None
        board = [
           ["", "", ""],
           ["", "", ""],
           ["", "", ""]
        ]

        for i in range(3):
            if all(board[i][j] == "X" for j in range(3)):
                winner = "X"

            elif all(board[i][j] == "O" for j in range(3)):
                winner = "O"

            elif all(board[j][i] == "X" for j in range(3)):
                winner = "X"

            elif all(board[j][i] == "O" for j in range(3)):
                winner = "O"