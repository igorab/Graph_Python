# 4.1 покрыть отрезки точками
n = int(input())
sectors = []
for i in range(n):
    l, r = map(int, input().split())
    sectors.append([l, r])

sectors.sort(key = lambda item: item[1] )

points = []
for sec in sectors:
    r = sec[1]
    points.append(r)

m = len(points)
print(m)
print(*points)