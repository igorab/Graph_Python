# 4.1 покрыть отрезки точками

# список один вложенный со всеми координатами, сортируем по правому концу,
# сравниваем правый и левый
# левый меньше или равен - идем дальше
# левый больше - добавляем новый правый(пару левого) в список точек


n = int(input())
sectors = []
for i in range(n):
    l, r = map(int, input().split())
    sectors.append([l, r])
#ужно отсортировать все отрезки по 2му аргументу
sectors.sort(key = lambda item: item[1] )

points = []
cur = 0
while cur < len(sectors):
    sec = sectors[cur]
    r = sec[1]
    for i in range(cur, len(sectors)):
        s2 = sectors[i]
        if r >= s2[0]:
            cur = cur + 1
            if (r not in points):
                points.append(r)
        else:
            break

m = len(points)
print(m)
print(*points)