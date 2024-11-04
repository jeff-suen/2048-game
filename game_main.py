from game_function import grid_init, grid_display, move, add_new_tile, check_win, check_game_over

class InvalidInputError(Exception):
    """Custom exception for invalid user input."""
    pass

def restart():
    """Prompting the user to restart or exit the game, with error handling for invalid input."""
    while True:
        try:
            choice = input("Would you like to restart the game? [yes/no]").strip().lower()
            if choice == 'yes':
                return True
            elif choice == 'no':
                print('Thank you for playing the game. Good bye!')
                return False
            else:
                raise InvalidInputError
        except InvalidInputError:
            print("Invalid input! Please input 'yes' to restart or 'no' to end the game.")

def main():
    grid = grid_init()
    add_new_tile(grid)
    add_new_tile(grid)

    while True:
        grid_display(grid)
        try:
            move_direction = input("Press w (up), s (down), a (left), or d (right) to move: ").strip().lower()

            if move_direction in ['w', 's', 'a', 'd']:
                if move(grid, move_direction):
                    add_new_tile(grid)
                    
                    if check_win(grid):
                        grid_display(grid)
                        print("Congratulations! You've reached 2048!")
                        if restart():
                            grid = grid_init()
                            add_new_tile(grid)
                            add_new_tile(grid)
                            continue
                        break

                    elif check_game_over(grid):
                        grid_display(grid)
                        print("Game over! No more moves available.")
                        if restart():
                            grid = grid_init()
                            add_new_tile(grid)
                            add_new_tile(grid)
                            continue
                        break
            else:
                raise InvalidInputError

        except InvalidInputError:
            print("Invalid input! Please use 'w', 's', 'a', or 'd'.")


if __name__ == "__main__":
    main()
