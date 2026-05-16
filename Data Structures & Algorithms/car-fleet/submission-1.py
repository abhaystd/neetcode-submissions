class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars_position = [(p,s) for p, s in zip(position, speed)]

        cars_position.sort( reverse = True)
        stack=[]
        res=0
        for pos, s in cars_position:
            time_to_reach= (target-pos)/s
            if len(stack) and stack[-1]>= time_to_reach:
                continue
            else:
                stack.append(time_to_reach)
                res+=1
        # TC O(n logn) and SC O(n)
        return res