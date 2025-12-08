class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root= TrieNode()
        for w in words:
            node = root
            for ch in w:
                if ch not in node.children:
                    node.children[ch]= TrieNode()
                node= node.children[ch]
            node.word=w
        
        self.result=[]
        m, n = len(board), len(board[0])

        def dfs(i,j,node):
            char=board[i][j]
            if char not in node.children:
                return
            nxt= node.children[char]

            if nxt.word:
                self.result.append(nxt.word)
                nxt.word = None

            board[i][j]='#'

            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and board[x][y] != '#':
                    dfs(x, y, nxt)

            board[i][j]=char

        for i in range(m):
            for j in range(n):
                dfs(i,j,root)
        
        return self.result
