class Game:

    def play_with(self, agent):
        board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        print("Welcome!")
        self.show_board_status(board)

    def show_board_status(self, board):
        print("  0    1   2 ")
        for i, line in enumerate(board):
            print(f"{i}  {' | '.join(line)}")
            if i < 2:
                print(" " + "-" * 13)

    def get_available_pos(self, board):
        available_pos = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    available_pos.append((i,j))
        
        return available_pos

    def check_win(self, board, player):
        # Vertical
        if (board[0][0] == player and board[0][1] == player and board[0][2] == player):
            return True
        if (board[1][0] == player and board[1][1] == player and board[1][2] == player):
            return True
        if (board[2][0] == player and board[2][1] == player and board[2][2] == player):
            return True
        
        # Horizontal
        if (board[0][0] == player and board[1][0] == player and board[2][0] == player):
            return True
        if (board[0][1] == player and board[1][1] == player and board[2][1] == player):
            return True
        if (board[0][2] == player and board[1][2] == player and board[2][2] == player):
            return True
        
        # Diagonal
        if (board[0][0] == player and board[1][1] == player and board[2][2] == player):
            return True
        if (board[0][2] == player and board[1][1] == player and board[2][0] == player):
            return True

        return False
