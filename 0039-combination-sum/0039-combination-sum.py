class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result=[]

        def solve(i,path,total):
            if total==target:
                result.append(path.copy())
                return
            if total>target or i==len(candidates):
                return

            path.append(candidates[i])
            solve(i,path,total+candidates[i])
            path.pop()
            solve(i+1,path,total)

        solve(0,[],0)
        return result


            
        