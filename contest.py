import sys
S = "loveleetcode"
C = 'e'
m = sys.maxsize
dic = []
res = []
for i in range(len(S)):
    if S[i] == C:
        dic.append(i)
print(dic)
for i in range(len(S)):
    for j in dic:
        m = min(abs(i -j), m)
    res.append(m)
    m = sys.maxsize
print(res)