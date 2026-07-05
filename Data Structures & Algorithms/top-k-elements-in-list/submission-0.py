class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map={}
        for i in nums:
            if i in freq_map:
                freq_map[i]+=1
            else:
                freq_map[i]=1
        sorted_items=sorted(freq_map.items(),key=lambda x: x[1],reverse=True)
        ans=[]
        for i in range(k):
            ans.append(sorted_items[i][0])
        return ans

        
    
        
        