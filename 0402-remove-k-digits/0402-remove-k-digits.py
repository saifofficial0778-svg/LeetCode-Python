class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for ch in num:
            while stack and stack[-1]>ch and k>0:
                stack.pop()
                k-=1
            stack.append(ch)

        while k>0:
            stack.pop()
            k-=1
        result ="".join(stack).lstrip('0')

        return result if result else "0"