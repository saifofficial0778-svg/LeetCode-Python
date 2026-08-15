class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        max_len=float('-inf')
        left=0
        mydict={}
        max_freq=0
        if s=="":
            return 0
        for right in range(0,n):
            if s[right] not in mydict:
                mydict[s[right]]=1
            else:
                mydict[s[right]]+=1

            while mydict[s[right]]>1:
                mydict[s[left]]-=1
                if mydict[s[left]]==0:
                    del mydict[s[left]]
                left+=1
            max_len=max(max_len,right-left+1)
        return max_len