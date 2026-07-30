class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mydict={}
        longest=0
        left=0

        for right in range(len(s)):
            if s[right] in mydict:
                left=max(left,mydict[s[right]]+1)
            longest=max(longest,right-left+1)
            mydict[s[right]]=right
        return longest
        