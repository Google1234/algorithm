class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        origin_x=(0+len(matrix)-1.0)/2
        origin_y=(0+len(matrix)-1.0)/2
        if len(matrix)%2==0:
            right=len(matrix)/2
            down=len(matrix)/2
        else:
            right=len(matrix)/2+1
            down=len(matrix)/2
        for x in xrange(right):
            for y in xrange(down):
                source_x=x
                source_y=y
                buff=matrix[source_x][source_y]
                for i in xrange(4):
                    desitination_x=int(origin_x+source_y-origin_y)
                    desitination_y=int(origin_y+origin_x-source_x)
                    buff2=matrix[desitination_x][desitination_y]
                    matrix[desitination_x][desitination_y]=buff
                    source_x=desitination_x
                    source_y=desitination_y
                    buff=buff2
        return matrix