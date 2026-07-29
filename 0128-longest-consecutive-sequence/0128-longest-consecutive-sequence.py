class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        last_smaller=float('inf')
        count=0
        longest=0
        nums.sort()
        

        for i in range(0,len(nums)):
            num=nums[i]
            if last_smaller==num-1:
                count+=1
                last_smaller=num
            elif num!=last_smaller:
                count=1
                last_smaller=num
            
           
            longest=max(count,longest)
        return longest