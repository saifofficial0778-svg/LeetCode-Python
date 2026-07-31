class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        mydict={}
        n=len(fruits)
        max_length=0
        left=0

        for right in range(n):
            if fruits[right] not in mydict:
                mydict[fruits[right]]=1
            else:
                mydict[fruits[right]]+=1
            while len(mydict) > 2:
                mydict[fruits[left]]-=1

                if mydict[fruits[left]]==0:
                    del mydict[fruits[left]]
                left+=1

            if len(mydict)<=2:
                max_length=max(max_length,right-left+1)
        return max_length

                