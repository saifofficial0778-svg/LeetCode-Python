class Solution:
    def firstUniqChar(self, s: str) -> int:
        mydict={}
        for ch in s:
            mydict[ch]=mydict.get(ch,0)+1

        for i in range(len(s)):
            if mydict[s[i]]==1:
                return i
        return -1