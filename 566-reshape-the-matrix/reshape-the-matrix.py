class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        rows=len(mat)
        cols=len(mat[0])

        if len(mat)*len(mat[0])!=r*c:
            return mat

        res=[[0]*c for _ in range(r)]

        index=0
        for i in range(rows):
            for j in range(cols):
                new_row=index//c
                new_col=index%c

                res[new_row][new_col]=mat[i][j]
                index+=1
        return res
        