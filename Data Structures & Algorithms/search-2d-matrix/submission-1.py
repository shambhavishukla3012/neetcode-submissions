class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # m, n = len(matrix), len(matrix[0])
        # l, r = 0, m*n-1

        # while l<=r:
        #     m = (l+r)//2
        #     row = m //n
        #     col = m % n

        #     val = matrix[row][col]

        #     if target > val:
        #         l = m+1
        #     elif target<val:
        #         r = m-1
        #     else:
        #         return True
        # return False


        top, bot = 0 , len(matrix)-1

        while top <= bot:
            mid_row = (top+bot)//2
            if target> matrix[mid_row][-1]:
                top = mid_row+1
            elif target< matrix[mid_row][0]:
                bot = mid_row-1
            else:
                break

        if not(top<=bot):
            return False
        
        cur_row =(top+bot)//2
        l, r = 0, len(matrix[0])-1
        while l<=r:
            m = (l+r)//2
            if target > matrix[cur_row][m]:
                l = m+1
            elif target < matrix[cur_row][m]:
                r =m-1
            else:
                return True
        return False

