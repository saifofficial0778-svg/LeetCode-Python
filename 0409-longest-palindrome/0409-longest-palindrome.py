class Solution:
    def longestPalindrome(self, s: str) -> int:
        mydict={}
        for ch in s:
            mydict[ch]=mydict.get(ch,0)+1

        odd=False
        ans=0

        for value in mydict.values():
            ans+=(value//2)*2
            if value%2==1:
                odd=True
        if odd:
            ans+=1
        return ans