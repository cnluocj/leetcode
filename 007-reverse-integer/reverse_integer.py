class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if type(x) != int:
        	return 0

        if not (-2**31 < x < 2**31-1):
        	return 0

        strx = str(x)

        restrx = ''
        isneg = False
        for item in strx:
        	if item == '-':
        		isneg = True
        	else:
        		restrx = item + restrx

        if isneg:
        	restrx = '-' + restrx

        x = int(restrx)

        if not (-2**31 < x < 2**31-1):
         	return 0

        return x