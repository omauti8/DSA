class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def back(curr,open_, close):
            if len(curr)== 2*n:
                res.append(curr)
                return

            if open_ < n:
                back(curr + '(', open_+1, close)

            if close < open_:
                back(curr + ')', open_, close+1)

        back("",0,0)
        return res     