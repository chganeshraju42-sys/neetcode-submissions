class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n=len(position)
        cars=[]
        for i in range(n):
            cars.append([position[i],speed[i]])
        cars.sort(key=lambda x:x[0],reverse=True)
        stk=[]
        for position,speed in cars:
            time=(target-position)/speed
            if not stk or time>stk[-1]:
                stk.append(time)
        return (len(stk))

        
        