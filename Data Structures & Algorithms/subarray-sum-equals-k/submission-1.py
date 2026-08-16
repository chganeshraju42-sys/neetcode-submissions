class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq={0:1}
        curr_num=0
        count=0
        for x in nums:
            curr_num+=x
            if curr_num-k in freq:
                count+=freq[curr_num-k]
            freq[curr_num]=freq.get(curr_num,0)+1
        return count