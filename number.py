class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)-1
        origin_x=(n*1.0)/2
        origin_y=(n*1.0)/2

        x=0
        y=0
        while x<origin_x:
            while y<origin_y:
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
                y+=1
            x+=1
s=Solution()
print s.rotate(([[1,2],[3,4]]))