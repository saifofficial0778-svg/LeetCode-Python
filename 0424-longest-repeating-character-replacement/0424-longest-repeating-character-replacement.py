class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mydict={}
        n=len(s)
        max_freq=0
        left=0
        max_len=float('-inf')
        for right in range(n):
            if s[right] not in mydict:
                mydict[s[right]]=1
            else:
                mydict[s[right]]+=1
            max_freq=max(max_freq,mydict[s[right]])

            while (right-left+1)-max_freq>k:
                mydict[s[left]]-=1
                if mydict[s[left]]==0:
                    del mydict[s[left]]
                left+=1
            max_len=max(max_len,right-left+1)
        return max_len
