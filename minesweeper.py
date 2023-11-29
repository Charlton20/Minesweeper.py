def print_grid(grid):
    for row in grid:
        print(" ".join(row))


def make_grid():
    minesweeper_grid = [
        ['#', '#', '-', '-', '-'],
        ['-', '-', '-', '-', '-'],
        ['-', '#', '#', '-', '#'],
        ['#', '-', '-', '-', '-'],
        ['-', '-', '#', '-', '-'],
    ]
    return minesweeper_grid


def reveal_cell(grid, x, y):
    if grid[x][y] == '#':
        print("Game Over! You hit a mine.")
        return True  # Game Over
    else:
        # Reveal the cell
        grid[x][y] = str(count_mines_around(grid, x, y))
        return False  # Continue playing


def count_mines_around(grid, x, y):
    count = 0
    for i in range(max(0, x - 1), min(len(grid), x + 2)):
        for j in range(max(0, y - 1), min(len(grid[0]), y + 2)):
            if grid[i][j] == '#':
                count += 1
    return count


def check_win(grid):
    for row in grid:
        if '-' in row:
            return False
    return True


def play_minesweeper():
    print("\n\t MINESWEEPER GRID\n_________________________")
    mine_grid = make_grid()
    revealed_cells = [[' ' for _ in range(len(mine_grid[0]))] for _ in range(len(mine_grid))]

    while True:
        print_grid(revealed_cells)
        x = int(input("Enter row (0 to {}): ".format(len(mine_grid) - 1)))
        y = int(input("Enter column (0 to {}): ".format(len(mine_grid[0]) - 1)))

        if x < 0 or x >= len(mine_grid) or y < 0 or y >= len(mine_grid[0]):
            print("Invalid input. Please enter valid row and column values.")
            continue

        if revealed_cells[x][y] != ' ':
            print("Cell already revealed. Choose another cell.")
            continue

        game_over = reveal_cell(mine_grid, x, y)
        if game_over:
            print_grid(mine_grid)
            print("You lost!")
            break

        if check_win(revealed_cells):
            print_grid(mine_grid)
            print("Congratulations! You won!")
            break

    print("Game Over.")


if __name__ == "__main__":
    play_minesweeper()
