class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length=0
        max_freq=0
        mydict={}
        left=0
        n=len(s)
        for right in range(n):
            if s[right] not in mydict:
                mydict[s[right]]=1
            else:
                mydict[s[right]]+=1
            max_freq=max(max_freq,mydict[s[right]])

            while (right-left+1)-max_freq>k:
                mydict[s[left]]-=1
                left+=1

            max_length=max(max_length,right-left+1)  
                
        return max_length