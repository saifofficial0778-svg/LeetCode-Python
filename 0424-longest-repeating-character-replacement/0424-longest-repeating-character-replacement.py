class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mydict={}
        left=0
        max_len=0
        max_freq=0
        freq=0           
        for right in range(len(s)):
            mydict[s[right]]=mydict.get(s[right],0)+1

            max_freq=max(max_freq,mydict[s[right]])

            while (right-left+1)-max_freq>k:
                mydict[s[left]]-=1

                if mydict[s[left]]==0:
                    del mydict[s[left]]
                left+=1
            max_len=max(max_len,right-left+1)

        return max_len





