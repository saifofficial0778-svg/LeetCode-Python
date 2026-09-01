class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        n=len(s)
        stack=[]

        for ch in s:
            if stack and stack[-1][0]==ch:
                stack[-1][1]+=1
            
                if stack[-1][1]==k:
                    stack.pop()

            else:
                stack.append([ch,1])
            
        res=""
        for ch , count in stack:
            res+=ch*count
        return res

        