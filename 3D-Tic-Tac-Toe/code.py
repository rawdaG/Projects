#!/usr/bin/env python3
from math import inf as infinity
from random import choice

# Constants
HUMAN = -1
COMP = +1
grid_size = 3  # Size of the 3D grid
board = [[[0 for _ in range(grid_size)] for _ in range(grid_size)] for _ in range(grid_size)]


def empty_cells(state):
    cells = []
    for z, plane in enumerate(state):
        for x, row in enumerate(plane):
            for y, cell in enumerate(row):
                if cell == 0:
                    cells.append([z, x, y])
    return cells


def wins(state, player):
    size = len(state)
    for z in range(size):
        for x in range(size):
            if all(state[z][x][y] == player for y in range(size)):
                return True
            if all(state[z][y][x] == player for y in range(size)):
                return True
        for y in range(size):
            if all(state[x][z][y] == player for x in range(size)):
                return True

    if all(state[i][i][i] == player for i in range(size)):
        return True
    if all(state[i][i][size - i - 1] == player for i in range(size)):
        return True
    if all(state[i][size - i - 1][i] == player for i in range(size)):
        return True
    if all(state[size - i - 1][i][i] == player for i in range(size)):
        return True

    return False


def game_over(state):
    return wins(state, HUMAN) or wins(state, COMP)


def evaluate(state):
    if wins(state, COMP):
        return +1
    elif wins(state, HUMAN):
        return -1
    else:
        return 0


def valid_move(z, x, y):
    return [z, x, y] in empty_cells(board)


def set_move(z, x, y, player):
    if valid_move(z, x, y):
        board[z][x][y] = player
        return True
    return False

def minimax(state, depth, player, alpha, beta):
    """
    AI function that chooses the best move using Minimax with Alpha-Beta Pruning.
    :param state: The current state of the board.
    :param depth: The depth of the decision tree.
    :param player: The current player (HUMAN or COMP).
    :param alpha: The best already-explored option for the maximizer.
    :param beta: The best already-explored option for the minimizer.
    :return: A list with [z, x, y, score].
    """
    if depth == 0 or game_over(state):
        return [-1, -1, -1, evaluate(state)]

    if player == COMP:
        best = [-1, -1, -1, -infinity]
        for cell in empty_cells(state):
            z, x, y = cell
            state[z][x][y] = player
            score = minimax(state, depth - 1, -player, alpha, beta)
            state[z][x][y] = 0
            score[0], score[1], score[2] = z, x, y

            if score[3] > best[3]:
                best = score
            alpha = max(alpha, best[3])
            if beta <= alpha:
                break
        return best
    else:
        best = [-1, -1, -1, +infinity]
        for cell in empty_cells(state):
            z, x, y = cell
            state[z][x][y] = player
            score = minimax(state, depth - 1, -player, alpha, beta)
            state[z][x][y] = 0
            score[0], score[1], score[2] = z, x, y

            if score[3] < best[3]:
                best = score
            beta = min(beta, best[3])
            if beta <= alpha:
                break
        return best


def render_3d_board(state):
    print("\n3D Tic Tac Toe Board:")
    for z, plane in enumerate(state):
        print(f"Layer {z + 1}:")
        for x in range(len(plane)):
            row = ""
            for y in range(len(plane[x])):
                cell = plane[x][y]
                if cell == HUMAN:
                    row += " X "
                elif cell == COMP:
                    row += " O "
                else:
                    row += "   "
                if y < len(plane[x]) - 1:
                    row += "|"
            print(row)
            if x < len(plane) - 1:
                print("---+---+---")
        print()

def ai_turn(c_choice, h_choice):
    """
    AI calculates and plays its move.
    :param c_choice: AI's choice (X or O).
    :param h_choice: Human's choice (X or O).
    """
    depth = 2  # Reduced depth for faster performance
    if len(empty_cells(board)) == grid_size ** 3:
        # Random move for the first turn
        z, x, y = choice(range(grid_size)), choice(range(grid_size)), choice(range(grid_size))
    else:
        move = minimax(board, depth, COMP, -infinity, +infinity)
        z, x, y = move[0], move[1], move[2]

    set_move(z, x, y, COMP)
    print(f"\nComputer moves to Layer {z + 1}, Row {x + 1}, Column {y + 1}")
    render_3d_board(board)


def human_turn(c_choice, h_choice):
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    while True:
        try:
            move = input('Enter your move as Layer,Row,Column (e.g., 1,2,3): ')
            z, x, y = map(int, move.split(","))
            if set_move(z - 1, x - 1, y - 1, HUMAN):
                break
            else:
                print("Invalid move. Try again.")
        except (ValueError, IndexError):
            print("Invalid format. Enter as Layer,Row,Column (e.g., 1,2,3).")

    print(f"\nYou moved to Layer {z}, Row {x}, Column {y}")
    render_3d_board(board)


def main():
    h_choice = ''  # X or O
    c_choice = ''  # X or O
    first = ''  # if human is the first

    while h_choice not in ['O', 'X']:
        h_choice = input('Choose X or O\nChosen: ').upper()

    c_choice = 'O' if h_choice == 'X' else 'X'

    while first not in ['Y', 'N']:
        first = input('First to start? [Y/N]: ').upper()

    human_first = first == 'Y'

    while len(empty_cells(board)) > 0 and not game_over(board):
        if human_first:
            human_turn(c_choice, h_choice)
            if game_over(board):
                break
            ai_turn(c_choice, h_choice)
        else:
            ai_turn(c_choice, h_choice)
            if game_over(board):
                break
            human_turn(c_choice, h_choice)

    if wins(board, HUMAN):
        print('YOU WIN!')
    elif wins(board, COMP):
        print('YOU LOSE!')
    else:
        print('DRAW!')


if __name__ == "__main__":
    main()
