class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res=0 
        for i in range(len(fruits)):
            group=set()
            j=i
            while j<len(fruits) and (len(group)<2 or fruits[j] in group):
                group.add(fruits[j])
                j+=1
                res=max(res,j-i)
        return res   



        