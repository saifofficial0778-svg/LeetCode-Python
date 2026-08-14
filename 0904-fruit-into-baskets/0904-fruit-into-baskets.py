class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_len=float('-inf')
        left=0
        n=len(fruits)
        mydict={}

        for right in range(n):
            if fruits[right] not in mydict:
                mydict[fruits[right]]=1
            else:
                mydict[fruits[right]]+=1

            while len(mydict)>2:
                mydict[fruits[left]]-=1

                if mydict[fruits[left]]==0:
                    del mydict[fruits[left]]
                left+=1

            max_len=max(max_len,right-left+1)
        return max_len

        
