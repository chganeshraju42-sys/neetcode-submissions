class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        n=len(nums)
        res=n//2
        for i in freq:
            if freq[i]>res:
                return i



        