class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars_position = [(p,s) for p, s in zip(position, speed)]

        cars_position.sort( reverse = True)
        prev_time=0
        res=0
        for pos, s in cars_position:
            time_to_reach = (target-pos)/s
            if prev_time and prev_time >= time_to_reach:
                continue
            else:
                prev_time = time_to_reach
                res+=1
        # TC O(n logn) and SC O(n)
        return res