import grpc
import time
import tic_tac_toe_pb2
import tic_tac_toe_pb2_grpc

def print_board(board):
    symbols = {0: '.', 1: 'X', 2: 'O'}
    for row in board:
        print(" ".join(symbols[cell] for cell in row))
    print()

def get_move(player):
    while True:
        try:
            y = int(input(f"Player {player} (X-coordinate): "))
            x = int(input(f"Player {player} (Y-coordinate): "))
            if 0 <= x < 3 and 0 <= y < 3:
                return x, y
            else:
                print("Coordinates should be between 0 and 2. Try again.")
        except ValueError:
            print("Invalid input. Please enter integers for coordinates.")

def update_board(board, flat_board):
    for i in range(3):
        for j in range(3):
            board[i][j] = flat_board[i * 3 + j]

def run():
    with grpc.insecure_channel('localhost:60052') as channel:
        stub = tic_tac_toe_pb2_grpc.TicTacToeStub(channel)
        
        response = stub.AssignPlayer(tic_tac_toe_pb2.AssignPlayerRequest())
        player = response.player_number
        print(f"Assigned player number: {player}")

        board = [[0] * 3 for _ in range(3)]
        
        while True:
            response = stub.CheckWinner(tic_tac_toe_pb2.CheckWinnerRequest())
            update_board(board, response.board)
            print_board(board)
            
            if response.winner != 0:
                print_board(board)
                if response.winner == 3:
                    print("The game is a draw!")
                else:
                    print(f"Player {response.winner} wins!")
                    time.sleep(5)
                break

            if response.current_player == player:
                x, y = get_move(player)
                response = stub.UserInput(tic_tac_toe_pb2.MoveRequest(player=player, row=x, column=y))
                if response.success:
                    board[x][y] = player
                else:
                    print(f"Move failed: {response.message}")
            else:
                print(f"Waiting for Player {response.current_player}'s move...")
                time.sleep(5)  # Polling interval

if __name__ == '__main__':
    run()
