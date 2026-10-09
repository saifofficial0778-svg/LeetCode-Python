class Solution:
    def longestPalindrome(self, s: str) -> int:
        mydict={}
        for ch in s:
            mydict[ch]=mydict.get(ch,0)+1

        odd=False
        ans=0
        for ch in mydict.values():
            ans+=(ch//2)*2

            if ch%2!=0:
                odd=True
        if odd:
            ans+=1
        return ans
            

