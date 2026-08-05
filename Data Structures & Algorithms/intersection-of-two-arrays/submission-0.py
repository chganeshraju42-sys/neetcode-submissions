class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set()
        res = []

        for i in nums2:
            if i in nums1 and i not in seen:
                res.append(i)
                seen.add(i)

        return res