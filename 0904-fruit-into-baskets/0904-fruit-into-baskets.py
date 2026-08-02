class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n=len(fruits)
        basket={}
        left=0
        length=0
        for right in range(n):
            if fruits[right] not in basket:
                    basket[fruits[right]]=1
            else:
                basket[fruits[right]]+=1
            
            while len(basket)>2:
                basket[fruits[left]]-=1

                if basket[fruits[left]]==0:
                    del basket[fruits[left]]
                left+=1
            if len(basket)<=2:    
                length=max(length,right-left+1)
        return length
                
       