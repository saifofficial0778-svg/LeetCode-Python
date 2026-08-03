class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1=len(t)
        n2=len(s)
        mydict={}
        for ch in t:
            if ch not in mydict:
                mydict[ch]=1
            else:
                mydict[ch]+=1

        min_len = float('inf')
        left=0
        matched=0
        for right in range(n2):
            if s[right] in mydict:
                mydict[s[right]]-=1
                if mydict[s[right]]>=0:
                    matched+=1
            while matched==len(t):
                if (right-left+1)<min_len:
                    min_len=right-left+1
                    start=left
                if s[left] in mydict:
                    mydict[s[left]]+=1
                    if mydict[s[left]]>0:
                        matched-=1
                left+=1
        if min_len==float('inf'):
            return ""
        return s[start:start+min_len]