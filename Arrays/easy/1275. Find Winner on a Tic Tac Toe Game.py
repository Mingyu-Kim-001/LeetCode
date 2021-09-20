class Solution:
    def find_winner(self, moves : List[List[int]]) -> str:
        moves_A = set([(x,y) for i, (x,y) in enumerate(moves) if i % 2 == 0])
        moves_B = set([(x,y) for i, (x,y) in enumerate(moves) if i % 2 == 1])
        for player, moves_each in (("A",moves_A), ("B",moves_B)):
            if all([(i,i) in moves_each for i in (0,1,2)]):
                return player
            if all([(i, 2 - i) in moves_each for i in (0,1,2)]):
                return player
            for i in (0,1,2):
                if all([(i,j) in moves_each for j in (0,1,2)]) or all([(j,i) in moves_each for j in (0,1,2)]):
                    return player
        return "Draw"
                
        
    def tictactoe(self, moves: List[List[int]]) -> str:
        winner = self.find_winner(moves)
        if winner == "Draw":
            return "Draw" if len(moves) == 9 else "Pending"
        return winner
        