class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        mydict={}

        for i in range(0,n):
            number=target-nums[i]

            if number not in mydict:
                mydict[nums[i]]=i
            else:
                return [mydict[number],i]
