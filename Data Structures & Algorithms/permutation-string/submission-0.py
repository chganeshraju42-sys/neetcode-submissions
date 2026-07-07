class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        freq_map={}
        for i in range(len(s1)):
            freq_map[s1[i]]=1+freq_map.get(s1[i],0)
        for i in range(len(s2)-len(s1)+1):
            freq_map1={}
            for j in range(i,i+len(s1)):
                freq_map1[s2[j]]=1+freq_map1.get(s2[j],0)
            if freq_map==freq_map1:
                return True
        return False
        
    


        