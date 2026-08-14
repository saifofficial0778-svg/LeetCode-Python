class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        fa=-1
        la=-1
        res=[]
        n=len(nums)
        low=0
        high=n-1
        low1=0
        high1=n-1

        while low<=high:
            mid=(low+high)//2
        
            if nums[mid]>=target:
                if nums[mid]==target:
                    fa=mid
                high=mid-1
                
            else:
                low=mid+1
        res.append(fa)

        while low1<=high1:
            mid1=(low1+high1)//2
            if nums[mid1]<=target:
                if nums[mid1]==target:
                    la=mid1
                low1=mid1+1
                
            else:
                high1=mid1-1
        res.append(la)
        return res

        

