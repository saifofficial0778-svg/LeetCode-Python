class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        res1=[]
        res2=[]

        for word in s:
            if word!='#':
                res1.append(word)
            elif word=='#' and len(res1)!=0:
                res1.pop()
        for word in t:
            if word!='#':
                res2.append(word)
            elif word=='#' and len(res2)!=0:
                res2.pop()
        if res1==res2:
            return True
        return False

