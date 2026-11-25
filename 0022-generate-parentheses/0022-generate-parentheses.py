class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result=[]
        brackets=[""]*2*n

        def solve(i,total,brackets):
            if i==len(brackets):
                if total==0:
                    result.append("".join(brackets))
                return
            if total<n:
                brackets[i]='('
                solve(i+1,total+1,brackets)

            if total>0:
                brackets[i]=')'
                solve(i+1,total-1,brackets)
        solve(0,0,brackets)
        return result