class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result=[]

        def backtrack(curr,open,close):
            if len(curr)==2*n:
                result.append(curr)
                return 

            if open<n:
                backtrack(curr+'(',open+1,close)

            if close<open:
                backtrack(curr+')',open,close+1)

        backtrack("",0,0)
        return result