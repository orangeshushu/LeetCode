'''
Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?
'''


class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        h = 0

        if n > 0:
            citations.reverse()
            while h < n and citations[h] >= h + 1:
                h += 1
            return h
        else:
            return 0