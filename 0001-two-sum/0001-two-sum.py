class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict={}

        for i in range(0,len(nums)):
            number=target-nums[i]

            if number in mydict:
                return [i,mydict[number]]
            else:
                mydict[nums[i]]=i