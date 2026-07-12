class Solution:
    def findMin(self, nums: List[int]) -> int:
        res=nums[0]
        low,high=0,len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[low]<=nums[mid]:
                res=min(res,nums[low])
                low=mid+1
            else:
                res=min(res,nums[mid])
                high=mid-1
                
        return res

        