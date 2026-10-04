class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]

        for ch in s:
            if stack and stack[-1][0]==ch:
                stack[-1][1]+=1
                if stack[-1][1]==k:
                    stack.pop()
            else:
                stack.append([ch,1])

        ans=""

        for ch , num in stack:
            ans+=ch*num
        return ans