class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums=[str(num)for num in nums]
        n=len(nums)

        for i in range(n):
            for j in range(0,n-i-1):
                if nums[j]+nums[j+1]<nums[j+1]+nums[j]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        ans="".join(nums)
        if ans[0]=='0':
            return '0'
        return ans
                
                