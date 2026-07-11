class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n=len(nums)
        k=k%n
        result=[]
        for i in range(n-k,n):
            result.append(nums[i])
        for i in range(0,n-k):
            result.append(nums[i])
        nums[:]=result