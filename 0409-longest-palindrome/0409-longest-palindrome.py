class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq={}

        for ch in s:
            freq[ch]=freq.get(ch,0)+1

        odd=False
        ans=0

        for count in freq.values():
            ans+=(count//2)*2
            if count%2==1:
                odd=True
        
        if odd:
            ans+=1
        return ans