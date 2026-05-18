class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        columns=len(matrix[0])
        rows=len(matrix)
        l=0
        r = (rows*columns) -1

        # for full sorted 2D matrix
        #  row = mid//columns and col=mid%columns
        while l<=r:
            mid=(l+r)//2
            row, col = mid//columns, mid%columns
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r=mid-1
            else:
                l=mid+1
        # TC O(log(m*n)) and SC O(1)
        return False
