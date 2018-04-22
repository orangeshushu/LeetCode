fronts = [1,2,4,4,7]
backs = [1,3,4,1,3]
res = fronts
res.extend(backs)
print(res)

m = min(res)
if res.count(m) == 1:
    print(m)
else:
    while m in res:
        res.remove(m)