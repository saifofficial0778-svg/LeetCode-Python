class Solution:
    def removeDuplicates(self, s: str) -> str:
        res=[]
        for i in range(len(s)):
            if len(res)>=1 and s[i]==res[-1]:
                res.pop()
            else:
                res.append(s[i])
        return "".join(res)