class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m_most=len(matrix)
        if m_most==0:
            return []
        else:
            n_most=len(matrix[0])
        t=0
        t_most=m_most*n_most
        layer_nd=0
        result = [0 for i in xrange(t_most)]
        while True:
            m=m_most-layer_nd
            n=n_most-layer_nd
            x=layer_nd
            y=layer_nd
            if t>=t_most:
                break
            while y<n:
                result[t]=matrix[x][y]
                y+=1
                t+=1
            y-=1
            x+=1
            if t>=t_most:
                break
            while x<m:
                result[t]=matrix[x][y]
                t+=1
                x+=1
            x-=1
            y-=1
            if t>=t_most:
                break
            while y>=layer_nd:
                result[t]=matrix[x][y]
                t+=1
                y-=1
            y+=1
            x-=1
            if t>=t_most:
                break
            while x>=layer_nd+1:
                result[t]=matrix[x][y]
                t+=1
                x-=1
            layer_nd+=1
        return result