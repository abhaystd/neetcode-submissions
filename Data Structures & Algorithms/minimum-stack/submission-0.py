class MinStack:

    def __init__(self):
        self.arr=[]
        self.min_arr=[]

    def push(self, val: int) -> None:
        stack=self.arr
        stack.append(val)

        if len(self.min_arr)!=0 and self.min_arr[-1]>=val:
            self.min_arr.append(val)
        elif len(self.min_arr)==0:
            self.min_arr.append(val)

    def pop(self) -> None:
        top_val=self.arr[-1]
        self.arr.pop()
        if top_val == self.min_arr[-1]:
            self.min_arr.pop()

        
    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.min_arr[-1]
        
