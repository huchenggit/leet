#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ret=[[]]
        for i in range(k):
            ret=[[j]+c for c in ret for j in range(1,c[0] if c else n+1)]
        return ret
t=Solution()
print(t.combine(4,2))
