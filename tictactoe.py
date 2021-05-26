import pygame

class Game:
    def draw_grid(self, window):
        """ draws the nine rectangle that create 3*3 game board and returns the list of python rectangle objects

        Args:
            window (pygame object): game screen where figures for game is drawn

        Returns:
            pygame object: rectangle forming game board
        """
        color = (255, 255, 255)
        grid = [(175 * y + 25, 175 * x + 25, 160, 160) for x in range(3) for y in range(3)]
        collision_grid = []
        for rectangle in grid:
            field = pygame.draw.rect(window, color, rectangle)
            collision_grid.append(field)
        pygame.display.update()

        return collision_grid

    def reset_board(self):
        """clears the board by setting all values of board to zero

        Returns:
            list: nested list(list of lists) having each element 0
        """
        return [[0 for i in range(3)] for j in range(3)]

    def reset_locked_positions(self):
        """sets all position of board to True

        Returns:
            list: list of len nine with all nine element equals to True
        """
        return [True for _ in range(3) for _ in range(3)]

    def check_all_positions(self, board):
        """loops through all the position in the board and checks whether any position is blank and returns true
        else returns False when board is full

        Args:
            board (List): 3*3 2D matrix storing selected coordinate for x or o

        Returns:
            Boolean : False if board is full else True
        """
        for row in board:
            for element in row:
                if element == 0:
                    return True
        return False

    def turn_text(self, window, board, font, player, game_winner, color=(255, 255, 255)):
        """ Displays the text stating the player whose has to perform the move and displays winner when
        winning condition is satisfied

        Args:
            window (pygame object): game screen where figures for game is drawn
            board (List): 3*3 2D matrix storing selected coordinate for x or o
            font (Object): Pygame Font object
            player (String): name of the player
            game_winner (Boolean): True if there is winner else False
            color (tuple, optional): RGB value. Defaults to (255, 255, 255).
        """
        sx = 435 // 2 - 35
        sy = 590
        pygame.draw.rect(window, (0, 0, 0), (sx, sy, 300, 50))
        if not game_winner:
            if self.check_all_positions(board):
                if player == "cross":
                    label = font.render("Human's turn", 1, color)
                else:
                    label = font.render("AI's turn", 1, color)
            else:
                label = font.render("Draw", 1, color)
            window.blit(label, (sx, sy))
        else:
            if player == "circle":
                label = font.render("Human wins", 1, color)
            else:
                label = font.render("AI wins", 1, color)
            window.blit(label, (sx, sy))

        pygame.display.update()

    def reset_text(self, window, font, color=(255, 255, 255)):
        """ displays the text message stating the way to reset board and restart the game

        Args:
            window (pygame object): game screen where figures for game is drawn
            font (Object): Pygame Font object
            color (tuple, optional): RGB value. Defaults to (255, 255, 255).
        """
        sx = 575
        sy = 450
        label_top = font.render("Press SPACE", True, color)
        label_bottom = font.render("to reset board", True, color)

        window.blit(label_top, (sx, sy))
        window.blit(label_bottom, (sx, sy + 50))

    def draw_winning_line(self, window, grid, winning_line, sign):
        """draws the red circle or cross when winning condition has reached

        Args:
            window (pygame object): game screen where figures for game is drawn
            grid (list): list of pygame rectangle object forming game board
            winning_line (List): list containing the elements that represent the position of winning line
            sign (String): name of player
        """
        for i in range(9):
            if i in winning_line:
                if sign == "cross":
                    self.draw_X(window, grid[i], (255, 0, 0))
                else:
                    self.draw_O(window, grid[i], (255, 0, 0))
        pygame.display.update()

    def win_check(self, board, player):
        """checks if game has meet winning condition

        Args:
            board (List): 3*3 2D matrix storing selected coordinate for x or o
            player (String): name of player

        Returns:
            Boolean, List: True if winning condition is satisfied and list of position value of winning moves
            else false and list with each element equal to -1
        """
        # Check rows
        query_field = 0
        for row in range(3):
            winning_line = []
            for field in range(3):
                if board[row][field] == player:
                    winning_line.append(query_field)
                query_field += 1
            if len(winning_line) == 3:
                return True, winning_line

        # Check columns
        query_field, next_field = 0, 0
        for column in range(3):
            winning_line = []
            query_field = next_field
            next_field += 1
            for row in board:
                if row[column] == player:
                    winning_line.append(query_field)
                query_field += 3
            if len(winning_line) == 3:
                return True, winning_line

        # Check diagonals
        query_field = 0
        winning_line = []
        for field in range(3):
            if board[field][field] == player:
                winning_line.append(query_field)
            query_field += 4
        if len(winning_line) == 3:
            return True, winning_line

        query_field = 2
        winning_line = []
        for field in range(3):
            if board[field][2 - field] == player:
                winning_line.append(query_field)
            query_field += 2
        if len(winning_line) == 3:
            return True, winning_line

        return False, [-1, -1, -1]

    def update_board(self, board, locked_positions, update_field, value):
        """ marks the board according to current player move and locked the position so that
         same move cannot be made again

        Args:
            board (List): 3*3 2D matrix storing selected coordinate for x or o
            locked_positions (List): list of len nine where elements are Boolean value indicating whether the position on the
                                        board is locked
            update_field (Integer): integer whose value range between 0-8
            value (String): name of Player
        """
        current_field = 0
        for row in range(3):
            for field in range(3):
                if update_field == current_field:
                    board[row][field] = value
                current_field += 1

        current_field = 0
        for query_position in range(9):
            if update_field == current_field:
                locked_positions[query_position] = False
            current_field += 1

    def draw_X(self, window, field, color=(0, 0, 0)):
        """draws the red X or red circle along the winning row,column or diagonal

        Args:
            window (pygame object): game screen where figures for game is drawn
            field ([type]): [description]
            color (tuple, optional): RGB Value. Defaults to (0, 0, 0).
        """
        x_start, y_start = field[0], field[1]
        x_start += 15
        y_start += 15
        start_point1 = (x_start, y_start)
        end_point1 = (x_start + 130, y_start + 130)
        pygame.draw.line(window, color, start_point1, end_point1, 10)
        start_point2 = (x_start, y_start + 130)
        end_point2 = (x_start + 130, y_start)
        pygame.draw.line(window, color, start_point2, end_point2, 10)

        pygame.display.update()

    def draw_O(self, window, field, color=(0, 0, 0)):
        """ draws circle to indicate the move of circle player

        Args:
            window (pygame object): game screen where figures for game is drawn
            field (List):
            color (tuple, optional): [description]. Defaults to (0, 0, 0).
        """
        x_center, y_center = field[0], field[1]
        x_center += 80
        y_center += 80
        radius = 65
        pygame.draw.circle(window, color, (x_center, y_center), radius, 7)

        pygame.display.update()

    def statistic(self, window, record, color=(255, 255, 255)):
        """ displays the game score

        Args:
            window (pygame object): game screen where figures for game is drawn
            record (List): List of length 3 where each element represent the score of AI, Human and draw respectively
            color (tuple, optional): RGB value. Defaults to (255, 255, 255).
        """
        font = pygame.font.SysFont("comicsans", 40, italic=True)
        sx = 550
        sy = 25
        pygame.draw.rect(window, color, (sx, sy, 335, 160), 3)
        pygame.draw.rect(window, (0, 0, 0), (sx + 5, sy + 5, 325, 150))
        label_X = font.render("Human:          " + str(record[0]), True, color)
        label_draw = font.render("Draw:             " + str(record[1]), True, color)
        label_O = font.render("AI:                 " + str(record[2]), True, color)

        window.blit(label_X, (sx + 10, sy + 10))
        window.blit(label_draw, (sx + 10, sy + 60))
        window.blit(label_O, (sx + 10, sy + 110))

        pygame.display.update()

    def draw_player(self, window, grid, board, locked_positions, mouse_position, draw_object):
        """Draws cross move of the player

        Args:
            window (pygame object): game screen where figures for game is drawn
            grid (list): list of pygame rectangle object forming game board
            board (List): 3*3 2D matrix storing selected coordinate for x or o
            locked_positions (List): list of len 9 containing each element equal to True or False
            mouse_position (Tuple): x and y coordinate of mouse click
            draw_object (String): name of figure(cross or circle) to be drawn

        Returns:
            String: name of player
        """
        query_field = 0
        for field, open_position in zip(grid, locked_positions):
            if field.collidepoint(mouse_position) and open_position:
                self.draw_X(window, field)
                draw_object = "circle"
                self.update_board(board, locked_positions, query_field, 1)
            query_field += 1
        return draw_object

    def draw_ai(self, window, grid, x, y, AI_object, board, locked_positions):
        """ marks the move of AI on board

        Args:
            window (pygame object): game screen where figures for game is drawn
            grid (list): list of pygame rectangle object forming game board
            x (Integer): value of x-coordinate of mouse click
            y (Integer): value of y-coordinate of mouse click
            board (List): 3*3 2D matrix storing selected coordinate for x or o
            locked_positions (List): list of len 9 containing each element equal to True or False

        Returns:
            String: name of player
        """
        index = 3 * x + y
        field = grid[index]
        self.draw_O(window, field)
        next_object = "cross"
        self.update_board(board, locked_positions, index, 2)
        return next_object
