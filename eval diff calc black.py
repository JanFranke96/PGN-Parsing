import chess.pgn
import chess.engine
import pickle
import time


def parse_time_to_seconds(time_str):
    # Split the time string into hours, minutes, and seconds
    hours, minutes, seconds = map(int, time_str.split(':'))
    # Calculate the total time in seconds
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

def extract_move_times(move_annotation):
    # Check if the move annotation contains '[%clk '
    if '[%clk ' in move_annotation:
        # Extract the move time
        move_time = move_annotation.split('[%clk ')[1].split(']')[0]
        return move_time
    else:
        return None  # Return None if no move annotation found


def check_if_ends2(board, move_count):
    if move_count == 58:
        if board.turn == chess.WHITE and 31 > board.fullmove_number > 9:
            return True
        else:
            return False
    elif move_count == 59:
        return False
    else: # Odd number of moves - White plays last
        if board.turn == chess.WHITE and 31 > board.fullmove_number > 9:
            return True
        else:
            return False

def check_if_mate30(board, move_count):
    if move_count == 59:
        return False
    else: # Odd number of moves - White plays last
        if board.turn == chess.BLACK and 30 > board.fullmove_number > 9:
            return True
        else:
            return False



def analyze_game(pgn_file):
    # Initialize Stockfish engine
    engine = chess.engine.SimpleEngine.popen_uci(
        "C:\\Users\\J.Franke\\PycharmProjects\\chessboard\\stockfish-windows-x86-64-avx2.exe")

    # Load PGN file
    eval_list = []
    runtime_list = []
    best_move_list = []
    with open(pgn_file) as f:
        while True:
            game = chess.pgn.read_game(f)
            if game is None:
                break

            move_count = sum(1 for _ in game.mainline_moves())

                # Check if the game has at least 30 moves
            if game.end().board().fullmove_number < 30:
                continue

            # Check if the time control is "600+0"
            if game.headers.get("TimeControl") != "180+0":
                continue

            node = game
            while node is not None:
                board = node.board()

                # Check if it's White's turn
                if check_if_mate30(board, move_count):

                    # Start clock for measuring Stockfish runtime
                    start_time = time.time()

                    # Analyze position with Stockfish
                    analysis = engine.analyse(board, chess.engine.Limit(depth=20))
                    eval_info = analysis["score"].relative.score(mate_score=10000)  # Extract engine evaluation
                    if eval_info is not None:
                        eval_info *= -1  # Multiply eval_info by -1
                        eval_list.append(eval_info)

                    # End clock and calculate runtime
                    end_time = time.time()
                    runtime = end_time - start_time
                    if runtime is not None:
                        runtime_list.append(runtime)

                    # Extract best move
                    best_move = analysis.get("pv", [])[0] if "pv" in analysis else None
                    best_move_list.append(best_move)

                # Move to the next node in the game
                node = node.next()

    # Close Stockfish engine
    engine.quit()

    return eval_list, runtime_list, best_move_list


def calculate_move_times(pgn_file):
    # Load PGN file
    movetime_list = []
    move_counter_list = []
    move_played_list = []  # List to store the move played for each position
    with open(pgn_file) as f:
        while True:
            game = chess.pgn.read_game(f)
            if game is None:
                break

            move_count = sum(1 for _ in game.mainline_moves())

                # Check if the game has at least 30 moves
            if game.end().board().fullmove_number < 30:
                continue

            # Check if the time control is "600+0"
            if game.headers.get("TimeControl") != "180+0":
                continue

            node = game
            prev_move_time = None
            while node is not None:
                board = node.board()

                # Check if it's White's turn
                if check_if_ends2(board, move_count):

                    move_time_str = extract_move_times(node.comment)
                    if move_time_str is not None:
                        move_time_seconds = parse_time_to_seconds(move_time_str)
                        if prev_move_time is not None:
                            # Calculate time spent on the move
                            time_spent = prev_move_time - move_time_seconds
                            movetime_list.append(time_spent)
                            move_counter_list.append(board.fullmove_number)
                            # Extract move played
                            move_played = node.move
                            move_played_list.append(move_played)
                        # Update previous move time
                        prev_move_time = move_time_seconds

                # Move to the next node in the game
                node = node.next()
        print("Number of elements in movetime_list:", len(movetime_list))  # Print the counter value

    return movetime_list, move_counter_list, move_played_list


# Example usage
pgn_file = "lichess_Elda64_2024-04-15.pgn"
eval_list_scriptblack, runtime_list, best_move_list = analyze_game(pgn_file)
# Print the number of elements in eval_list_scriptwhite
print("Number of elements in eval_list:", len(eval_list_scriptblack))
movetime_list, move_counter_list, move_played_list = calculate_move_times(pgn_file)


# Combine movetime_list, move_counter_list, and eval_list_scriptwhite into a list of coordinates
coordinates = list(zip(move_counter_list, movetime_list, eval_list_scriptblack))
print(move_played_list)
print(best_move_list)
print(coordinates)

save_location = "C:\\Users\\J.Franke\\PycharmProjects\\chessboard"

with open(save_location + "timeandeval_black3min.pkl", "wb") as f:
    pickle.dump(coordinates, f)

# Combine movetime_list, move_counter_list, and eval_list_scriptwhite into a list of coordinates
coordinates = list(zip(move_counter_list, movetime_list, eval_list_scriptblack))


save_location = "C:\\Users\\J.Franke\\PycharmProjects\\chessboard"

with open(save_location + "timeandeval_black10min.pkl", "wb") as f:
    pickle.dump(coordinates, f)
