class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars={}
        for i in range(len(position)):
            cars[position[i]]=speed[i]
        
        cars_position =dict(sorted(cars.items(),reverse=True))
        # print(cars_position)
        stack=[]
        res=0
        for i, (pos, s) in enumerate(cars_position.items()):
            time_to_reach= (target-pos)/s
            if len(stack) and stack[-1]>= time_to_reach:
                continue
            else:
                stack.append(time_to_reach)
                res+=1

        return res