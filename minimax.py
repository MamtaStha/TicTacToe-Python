class MiniMax:
    """
    class containing implementation of MiniMax Alogrithm
    """

    def optimal_move(self, board):
        """
        returns the optimal move for the computer

        Args:
            board (List): 3*3 2D matrix storing selected coordinate for x or o

        Returns:
            List: coordinate of optimal move
        """

        best_score = float("-inf")
        best_move = [-1, -1]
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 2
                    score = self.minimax(board, 0, False)
                    board[i][j] = 0
                    if score > best_score:
                        best_score = score
                        best_move = [i, j]
        return best_move

    def minimax(self, board, depth, is_maximizing):
        """
        returns score at each node

        Args:
            board (List): 3*3 2D matrix storing selected coordinate for x or o
            depth (Int): depth of tree
            is_maximizing (bool): check whether maximising or not

        Returns:
            Int: score of each node
        """
        result = self.check_win(board)
        if result != -2:
            return result

        if is_maximizing:
            best_score = float("-inf")
            for i in range(3):
                for j in range(3):
                    # Check for available spot
                    if board[i][j] == 0:
                        board[i][j] = 2
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = 0
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(3):
                for j in range(3):
                    # Check for available spot
                    if board[i][j] == 0:
                        board[i][j] = 1
                        score = self.minimax(board, depth + 1, True)
                        board[i][j] = 0
                        best_score = min(score, best_score)
            return best_score

    def check_win(self, board):
        """
        check who wins or draw and return score

        Args:
            board (List): 3*3 2D matrix storing selected coordinate for x or o

        Returns:
            Int: score according to who wins or draw
        """
        scores = [0, -1, 1]
        # Horizontal
        for i in range(3):
            if board[i][0] != 0 and board[i][0] == board[i][1] == board[i][2]:
                return scores[board[i][0]]
        # Vertical
        for i in range(3):
            if board[0][i] != 0 and board[0][i] == board[1][i] == board[2][i]:
                return scores[board[0][i]]
        # Diagonal
        if board[0][0] != 0 and board[0][0] == board[1][1] == board[2][2]:
            return scores[board[0][0]]
        if board[2][0] != 0 and board[2][0] == board[1][1] == board[0][2]:
            return scores[board[2][0]]

        # Check for draw
        open_spots = 0
        for row in board:
            for element in row:
                if element == 0:
                    open_spots += 1

        if open_spots == 0:
            return 0
        else:
            return -2
