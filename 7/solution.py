class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
            
        b =[int(y) for y in str(abs(x))]
        b.reverse()
       
        if int(''.join(map(str,b))) <= ((1 << 31)-1):
            if x < 0:
                return (str(-1*int(''.join(map(str,b)))))
            else:
                return(str(int(''.join(map(str,b)))))
        else:
            return ('0')