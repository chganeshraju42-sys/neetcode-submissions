class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not  nums:
            return 0
        n=len(nums)
        max_count=1
        for i in range(0,n):
            num=nums[i]
            count=1
            while num+1 in nums:
                count +=1
                num +=1
            max_count=max(max_count,count)
        return max_count        