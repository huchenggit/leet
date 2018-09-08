class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math
        lst_n = [str(i) for i in range(1, n + 1)]
        res = ''
        for i in range(1, n)[::-1]:
            index = math.ceil(k / math.factorial(i)) - 1
            res += lst_n.pop(index)
            k = k - math.factorial(i) * index
        res += lst_n[0]
        return res