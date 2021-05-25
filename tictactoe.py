import pygame


class Game:

    #drawing 3x3 matrix for our game board.
    def draw_grid(self, window):
        """[summary]

        Args:
            window ([type]): [description]

        Returns:
            [type]: [description]
        """
        color = (255, 255, 255)
        grid = [
            (175 * y + 25, 175 * x + 25, 160, 160) for x in range(3) for y in range(3)
        ]
        collision_grid = []
        for rectangle in grid:
            field = pygame.draw.rect(window, color, rectangle)
            collision_grid.append(field)
        pygame.display.update()

        return collision_grid

    def reset_board(self):
        #reset the board. _ is an instant variable created by python which is not used latter in any part of code.
        """[summary]

        Returns:
            [type]: [description]
        """
        return [[0 for _ in range(3)] for _ in range(3)]

    def reset_locked_positions(self):
        #resets all the locked position. Checks through each matrix value if True .It resets the locked position.
        """[summary]

        Returns:
            [type]: [description]
        """
        return [True for _ in range(3) for _ in range(3)]

    def check_all_positions(self, board):
        #loop through all the matrix value to check if the position value is True or Fals
        """[summary]

        Args:
            board ([type]): [description]

        Returns:
            [type]: [description]
        """
        for row in board:
            for element in row:
                if element == 0:
                    return True
        return False

    def turn_text(
        self, window, board, font, player, game_winner, color=(255, 255, 255)
    ):
        #displays the text indiaction the player
        """[summary]

        Args:
            window ([type]): [description]
            board ([type]): [description]
            font ([type]): [description]
            player ([type]): [description]
            game_winner ([type]): [description]
            color (tuple, optional): [description]. Defaults to (255, 255, 255).
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

        #reset the text when the new game is available for new game.
        """[summary]

        Args:
            window ([type]): [description]
            font ([type]): [description]
            color (tuple, optional): [description]. Defaults to (255, 255, 255).
        """
        sx = 575
        sy = 450
        label_top = font.render("Press SPACE", True, color)
        label_bottom = font.render("to reset board", True, color)

        window.blit(label_top, (sx, sy))
        window.blit(label_bottom, (sx, sy + 50))

    def draw_winning_line(self, window, grid, winning_line, sign):
        #Winning player will be indicated with different color. 
        """[summary]

        Args:
            window ([type]): [description]
            grid ([type]): [description]
            winning_line ([type]): [description]
            sign ([type]): [description]
        """
        for i in range(9):
            if i in winning_line:
                if sign == "cross":
                    self.draw_X(window, grid[i], (255, 0, 0))
                else:
                    self.draw_O(window, grid[i], (255, 0, 0))
        pygame.display.update()

    def win_check(self, board, player):
        #befeor next move program is is checking if any of the player have won the game.
        """[summary]

        Args:
            board ([type]): [description]
            player ([type]): [description]

        Returns:
            [type]: [description]
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
        #updating the value of an empyty feild.
        """[summary]

        Args:
            board ([type]): [description]
            locked_positions ([type]): [description]
            update_field ([type]): [description]
            value ([type]): [description]
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
        #desiginig X
        """[summary]

        Args:
            window ([type]): [description]
            field ([type]): [description]
            color (tuple, optional): [description]. Defaults to (0, 0, 0).
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
        #designing O
        """[summary]

        Args:
            window ([type]): [description]
            field ([type]): [description]
            color (tuple, optional): [description]. Defaults to (0, 0, 0).
        """
        x_center, y_center = field[0], field[1]
        x_center += 80
        y_center += 80
        radius = 65
        pygame.draw.circle(window, color, (x_center, y_center), radius, 7)

        pygame.display.update()

    def statistic(self, window, record, color=(255, 255, 255)):
        #creating display for statitcs
        """[summary]

        Args:
            window ([type]): [description]
            record ([type]): [description]
            color (tuple, optional): [description]. Defaults to (255, 255, 255).
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

    def draw_player(
        self, window, grid, board, locked_positions, mouse_position, draw_object
    ):
    #draw x 
        """[summary]

        Args:
            window ([type]): [description]
            grid ([type]): [description]
            board ([type]): [description]
            locked_positions ([type]): [description]
            mouse_position ([type]): [description]
            draw_object ([type]): [description]

        Returns:
            [type]: [description]
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

        #draw O
        """

        Args:
            window ([type]): [description]
            grid ([type]): [description]
            x ([type]): [description]
            y ([type]): [description]
            AI_object ([type]): [description]
            board ([type]): [description]
            locked_positions ([type]): [description]

        Returns:
            [type]: [description]
        """
        index = 3 * x + y
        field = grid[index]
        self.draw_O(window, field)
        next_object = "cross"
        self.update_board(board, locked_positions, index, 2)
        return next_object
