from typing import List
class Solution:
    def exist(self,board:List[List[str]],word:str)->bool:
        ROWS,COLS = len(board),len(board[0])
        path = set()


        def dfs(r,c,i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c>= COLS or word[i] != board[r][c] or (r,c) in path):
                return False
            

            path.add((r,c))
            result = (dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1 ))
            path.remove((r,c))
            return result
        

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):return True
        return False


if __name__ == "__main__":
    s = Solution()
    #Example1
    board1= [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word1 = "ABCCED"
    print(s.exist(board1,word1))

    #Example2
    board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word2 = "SEE"
    print(s.exist(board2,word2))

    #Example3
    board3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
    word3 = "ABCB" 
    print(s.exist(board3,word3))



              



