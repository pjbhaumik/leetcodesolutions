class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        _map = {}
        for i in range(len(s)):
            _map[i] = s[i]
        
        if numRows == 1 or len(s) == 1:
            return s
        
        if numRows == 2:
            body = 2
        else:    
            body = 2*numRows - 2
        rows = []
        
        for i in range(numRows):
            if i == 0:
                rows.append([i for i in range(len(_map)) if (i%body) == 0])
            elif i != numRows - 1:
                rows.append(sorted(list(set([z for row in rows[0] for z in [row+i, row+body-i] if z > 0 and z < len(_map)]))))
            else:
                rows.append([row + numRows -1 for row in rows[0] if row + numRows -1 < len(_map)])
        
        return ''.join([_map[x] for row in rows for x in sorted(row)])
        