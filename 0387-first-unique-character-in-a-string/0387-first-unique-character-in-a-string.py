class Solution:
    def firstUniqChar(self, s: str) -> int:
        mydict={}
        for i in range(len(s)):
            if s[i] not in mydict:
                mydict[s[i]]=1
            else:
                mydict[s[i]]+=1
        for i in range(len(s)):
            if mydict[s[i]]==1:
                return i
                break
        return -1