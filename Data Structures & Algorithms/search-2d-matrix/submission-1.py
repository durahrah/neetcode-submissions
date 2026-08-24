class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #double linear search, one on rows, one on the row itself
        top,bot = 0, len(matrix)-1
        row,col = len(matrix), len(matrix[0])-1

        while top<=bot:
            mid = (top + bot) //2
            if (target > matrix[mid][col]):
                top = mid+1
            elif (target<matrix[mid][0]):
                bot = mid - 1
            else:
                break

        if not top<=bot: #ie we got out of the while loop cause condition is false
            return False
        else:
            l,r= 0,col
            while l<=r:
                middie= (l+r)//2
                if (target>matrix[mid][middie]):
                    l = middie + 1
                elif (target<matrix[mid][middie]):
                    r = middie - 1
                else:
                    return True
            return False                



