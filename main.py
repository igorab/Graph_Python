def connected_components(graph):
    def visit(v):
        visited[v] = 1
        for w in graph[v]:
            if not visited[w]:
                visit(w)

    visited = [0 for _ in range(len(graph))]
    cc = 0

    for i in range(len(graph)):
        if not visited[i]:
            visit(i)
            cc += 1

    return cc

v, e = map(int, input().split())
graph = [[] for _ in range(v)]
for _ in range(e):
    x, y = map(int, input().split())
    graph[x - 1].append(y - 1)
    graph[y - 1].append(x - 1)

print(connected_components(graph))