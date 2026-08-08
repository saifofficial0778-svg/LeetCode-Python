class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        mydict={}
        max_freq=-1
        left=0
        max_len=-1
        for right in range(0,n):
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
