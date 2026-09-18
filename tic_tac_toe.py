# ============================================================
# CODSOFT AI Internship - Task 2
# Tic-Tac-Toe AI using Minimax Algorithm
# ============================================================

import math


# ------------------------------------------------------------
# Display the game board
# ------------------------------------------------------------
def print_board(board):
    print("\n")
    print("-------------")

    for i in range(3):
        print(
            "| " + board[i][0] +
            " | " + board[i][1] +
            " | " + board[i][2] + " |"
        )
        print("-------------")

    print()


# ------------------------------------------------------------
# Check whether a player has won
# ------------------------------------------------------------
def check_winner(board, player):
    # Check rows
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            return True

    # Check columns
    for col in range(3):
        if (
            board[0][col] == player
            and board[1][col] == player
            and board[2][col] == player
        ):
            return True

    # Check diagonals
    if (
        board[0][0] == player
        and board[1][1] == player
        and board[2][2] == player
    ):
        return True

    if (
        board[0][2] == player
        and board[1][1] == player
        and board[2][0] == player
    ):
        return True

    return False


# ------------------------------------------------------------
# Check whether the board is full
# ------------------------------------------------------------
def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False

    return True


# ------------------------------------------------------------
# Get all available moves
# ------------------------------------------------------------
def get_available_moves(board):
    moves = []

    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                moves.append((row, col))

    return moves


# ------------------------------------------------------------
# Minimax Algorithm
# ------------------------------------------------------------
def minimax(board, depth, is_maximizing):
    # AI wins
    if check_winner(board, "O"):
        return 10 - depth

    # Human wins
    if check_winner(board, "X"):
        return depth - 10

    # Draw
    if is_board_full(board):
        return 0

    # Maximizing player - AI
    if is_maximizing:
        best_score = -math.inf

        for row, col in get_available_moves(board):
            board[row][col] = "O"

            score = minimax(board, depth + 1, False)

            board[row][col] = " "

            best_score = max(best_score, score)

        return best_score

    # Minimizing player - Human
    else:
        best_score = math.inf

        for row, col in get_available_moves(board):
            board[row][col] = "X"

            score = minimax(board, depth + 1, True)

            board[row][col] = " "

            best_score = min(best_score, score)

        return best_score


# ------------------------------------------------------------
# Find the best move for AI
# ------------------------------------------------------------
def get_best_move(board):
    best_score = -math.inf
    best_move = None

    for row, col in get_available_moves(board):
        board[row][col] = "O"

        score = minimax(board, 0, False)

        board[row][col] = " "

        if score > best_score:
            best_score = score
            best_move = (row, col)

    return best_move


# ------------------------------------------------------------
# Convert position number into row and column
# ------------------------------------------------------------
def get_position_coordinates(position):
    position -= 1

    row = position // 3
    col = position % 3

    return row, col


# ------------------------------------------------------------
# Human player's move
# ------------------------------------------------------------
def human_move(board):
    while True:
        try:
            position = int(input("Enter your position (1-9): "))

            if position < 1 or position > 9:
                print("Please enter a number between 1 and 9.")
                continue

            row, col = get_position_coordinates(position)

            if board[row][col] != " ":
                print("That position is already occupied. Choose another.")
                continue

            board[row][col] = "X"
            break

        except ValueError:
            print("Invalid input! Please enter a number from 1 to 9.")


# ------------------------------------------------------------
# AI player's move
# ------------------------------------------------------------
def ai_move(board):
    print("AI is thinking...")

    best_move = get_best_move(board)

    if best_move is not None:
        row, col = best_move
        board[row][col] = "O"

        print(
            f"AI selected position: {(row * 3) + col + 1}"
        )


# ------------------------------------------------------------
# Display instructions
# ------------------------------------------------------------
def display_instructions():
    print("\n========== HOW TO PLAY ==========")
    print("You are X")
    print("AI is O")
    print()
    print("Use the following position numbers:")
    print()
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    print()
    print("Try to get three X's in a row!")
    print("=================================\n")


# ------------------------------------------------------------
# Play one game
# ------------------------------------------------------------
def play_game():
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    display_instructions()
    print_board(board)

    while True:
        # Human turn
        print("Your turn.")
        human_move(board)
        print_board(board)

        # Check human win
        if check_winner(board, "X"):
            print("🎉 Congratulations! You won!")
            break

        # Check draw
        if is_board_full(board):
            print("🤝 The game is a draw!")
            break

        # AI turn
        ai_move(board)
        print_board(board)

        # Check AI win
        if check_winner(board, "O"):
            print("🤖 AI wins! Better luck next time.")
            break

        # Check draw
        if is_board_full(board):
            print("🤝 The game is a draw!")
            break


# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------
def main():
    print("\n======================================")
    print("      TIC-TAC-TOE AI GAME")
    print("      CODSOFT AI INTERNSHIP")
    print("======================================")

    while True:
        play_game()

        while True:
            choice = input(
                "\nDo you want to play again? (yes/no): "
            ).strip().lower()

            if choice in ["yes", "y"]:
                break

            elif choice in ["no", "n"]:
                print("\nThank you for playing!")
                print("Goodbye! 👋")
                return

            else:
                print("Please enter yes or no.")


# ------------------------------------------------------------
# Program Entry Point
# ------------------------------------------------------------
if __name__ == "__main__":
    main()