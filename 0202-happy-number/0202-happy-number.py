class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            curr_sum=0
            while n>=1:
                ld=n%10
                curr_sum+=ld*ld
                n=n//10
            return curr_sum
        
        slow=n
        fast=get_next(n)

        while fast!=1 and slow!=fast:
            slow=get_next(slow)
            fast=get_next(get_next(fast))
        return fast==1

        
        