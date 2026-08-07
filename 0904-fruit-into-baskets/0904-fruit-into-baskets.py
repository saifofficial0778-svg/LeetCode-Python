class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket={}
        n=len(fruits)
        left=0
        max_len=0
        for right in range(0,n):
            if fruits[right] not in basket:
                basket[fruits[right]]=1
            else:
                basket[fruits[right]]+=1
            while len(basket)>2:
                basket[fruits[left]]-=1
                if basket[fruits[left]]==0:
                    del basket[fruits[left]]
                left+=1
            max_len=max(max_len,right-left+1)
        return max_len
        