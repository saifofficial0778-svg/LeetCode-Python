class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mydict={}
        for i in range(len(t)):
            if t[i] not in mydict:
                mydict[t[i]]=1
            else:
                mydict[t[i]]+=1
        matched=0
        left=0
        min_len=float('inf')
        for right in range(len(s)):
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



