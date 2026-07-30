class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            sum=0
            while n>0:
                ld=n%10
                sum+=ld*ld
                n=n//10
            return sum
        slow=n
        fast=get_next(n)
        while fast!=1 and slow!=fast:
            slow=get_next(slow)
            fast=get_next(get_next(fast))
        return fast==1
        