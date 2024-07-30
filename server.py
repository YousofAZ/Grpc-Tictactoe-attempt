from concurrent import futures
import grpc
import tic_tac_toe_pb2
import tic_tac_toe_pb2_grpc
import threading

class TicTacToeServicer(tic_tac_toe_pb2_grpc.TicTacToeServicer):
    def __init__(self):
        self.board = [[0] * 3 for _ in range(3)]
        self.current_player = 1
        self.player_count = 0
        self.lock = threading.Lock()

    def AssignPlayer(self, request, context):
        with self.lock:
            self.player_count += 1
            player_number = self.player_count
            print(f"Assigning player number: {player_number}")
            return tic_tac_toe_pb2.AssignPlayerResponse(player_number=player_number)

    def UserInput(self, request, context):
        print(f"Player {request.player} is trying to move to ({request.row}, {request.column})")
        print("Current board state:")
        for row in self.board:
            print(row)
        
        if self.board[request.row][request.column] != 0:
            print("Move is Invalid: Cell is already occupied.")
            return tic_tac_toe_pb2.MoveResponse(success=False, message="Move is Invalid")

        if request.player != self.current_player:
            print(f"Move is Invalid: It's not player {request.player}'s turn.")
            return tic_tac_toe_pb2.MoveResponse(success=False, message="It's not your turn.")

        self.board[request.row][request.column] = request.player
        self.current_player = 3 - request.player  # Switch player
        print("Move Applied")
        return tic_tac_toe_pb2.MoveResponse(success=True, message="Move Applied")

    def CheckWinner(self, request, context):
        winner = 0
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != 0:
                winner = self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != 0:
                winner = self.board[0][i]
        
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            winner = self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            winner = self.board[0][2]
        
        if winner == 0 and all(cell != 0 for row in self.board for cell in row):
            winner = 3  # Draw
        
        flat_board = [cell for row in self.board for cell in row]
        return tic_tac_toe_pb2.CheckWinnerResponse(winner=winner, board=flat_board, current_player=self.current_player)
    

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tic_tac_toe_pb2_grpc.add_TicTacToeServicer_to_server(TicTacToeServicer(), server)
    server.add_insecure_port('[::]:60052')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
