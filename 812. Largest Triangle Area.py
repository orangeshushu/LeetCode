'''
You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation:
The five points are show in the figure below. The red triangle is the largest.


Notes:
3 <= points.length <= 50.
No points will be duplicated.
 -50 <= points[i][j] <= 50.
Answers within 10^-6 of the true value will be accepted as correct.
'''
import math

class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        maxarea = 0
        for p1 in range(len(points)):
            for p2 in range(p1 + 1,len(points) - 1):
                for p3 in range(1 + p2, len(points)):
                    p1p2 = math.sqrt(pow((points[p1][0] - points[p2][0]), 2) + pow((points[p1][1] - points[p2][1]), 2))
                    p1p3 = math.sqrt(pow((points[p1][0] - points[p3][0]), 2) + pow((points[p1][1] - points[p3][1]), 2))
                    p2p3 = math.sqrt(pow((points[p2][0] - points[p3][0]), 2) + pow((points[p2][1] - points[p3][1]), 2))
                    if (p1p2 + p1p3 > p2p3) and (p1p2 + p2p3 > p1p3) and (p1p3 + p2p3 > p1p2):
                        s = (p1p2 + p1p3 + p2p3)/2
                        area = math.sqrt(s*(s-p1p2)*(s-p1p3)*(s-p2p3))
                        if maxarea < area:
                            maxarea = area
        return maxarea