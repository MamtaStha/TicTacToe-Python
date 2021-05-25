import pygame
import tictactoe
import minimax


def main():
    """[summary]"""
    minimax_algorithm = minimax.MiniMax()
    game = tictactoe.Game()

    pygame.init()

    window_width, window_height = 900, 685
    game_window = pygame.display.set_mode((window_width, window_height))
    game_window.fill((0, 0, 0))
    pygame.display.set_caption("Tic Tac Toe")
    game_font = pygame.font.SysFont("comicsans", 60)

    game_board = game.reset_board()
    game_grid = game.draw_grid(game_window)

    # cross - human;    circle - AI
    current_object = "cross"  # cross/circle

    run, winner = True, False
    game_locked_positions = game.reset_locked_positions()
    game_record = [0, 0, 0]
    change_record = True

    while run:
        pygame.time.delay(27)

        game.statistic(game_window, game_record)
        game.turn_text(game_window, game_board, game_font, current_object, winner)
        game.reset_text(game_window, game_font)

        for event in pygame.event.get():
            # Quit event
            if event.type == pygame.QUIT:
                run = False

            # Reset event
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_board = game.reset_board()
                    game_locked_positions = game.reset_locked_positions()
                    run, winner = True, False
                    change_record = True
                    game_grid = game.draw_grid(game_window)

            if (
                event.type == pygame.MOUSEBUTTONUP
                and current_object == "cross"
                and game.check_all_positions(game_board)
            ):
                game.turn_text(
                    game_window, game_board, game_font, current_object, winner
                )
                position = pygame.mouse.get_pos()

                if not winner:
                    current_object = game.draw_player(
                        game_window,
                        game_grid,
                        game_board,
                        game_locked_positions,
                        position,
                        current_object,
                    )
            elif current_object == "circle" and game.check_all_positions(game_board):
                game.turn_text(
                    game_window, game_board, game_font, current_object, winner
                )
                position = minimax_algorithm.optimal_move(game_board)
                if not winner:
                    current_object = game.draw_ai(
                        game_window,
                        game_grid,
                        position[0],
                        position[1],
                        current_object,
                        game_board,
                        game_locked_positions,
                    )

        win, win_line = game.win_check(game_board, 1)
        if win:
            winner = True
            game.draw_winning_line(game_window, game_grid, win_line, "cross")
            current_object = "circle"
            if change_record:
                game_record[0] += 1
                change_record = False
        win, win_line = game.win_check(game_board, 2)
        if win:
            winner = True
            game.draw_winning_line(game_window, game_grid, win_line, "circle")
            current_object = "cross"
            if change_record:
                game_record[2] += 1
                change_record = False

        if change_record:
            all_locked_positions = 0
            for locked_position in game_locked_positions:
                if locked_position:
                    break
                all_locked_positions += 1
            if all_locked_positions == 9:
                game_record[1] += 1
                change_record = False

        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
