import math
points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
maxarea = 0
for p1 in range(len(points)):
    p2 = p1 + 1
    p3 = len(points) - 1
    while p2 < p3:
        p1p2 = math.sqrt(pow((points[p1][0] - points[p2][0]), 2) + pow((points[p1][1] - points[p2][1]), 2))
        p1p3 = math.sqrt(pow((points[p1][0] - points[p3][0]), 2) + pow((points[p1][1] - points[p3][1]), 2))
        p2p3 = math.sqrt(pow((points[p2][0] - points[p3][0]), 2) + pow((points[p2][1] - points[p3][1]), 2))
        if (p1p2 + p1p3 > p2p3) and (p1p2 + p2p3 > p1p3) and (p1p3 + p2p3 > p1p2):
            s = (p1p2 + p1p3 + p2p3)/2
            area = math.sqrt(s*(s-p1p2)*(s-p1p3)*(s-p2p3))
            if maxarea < area:
                maxarea = area
        p2 = p2 + 1
print(maxarea)
