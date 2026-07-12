class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        
        while l<=r:
            mid=(l+r)//2
            day_count=1
            t_w=0
            for w in weights:
                t_w+=w
                if t_w>mid:
                    day_count+=1
                    t_w=w
            if day_count>days:
                l=mid+1
            else:
                r=mid-1
        return l