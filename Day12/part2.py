from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def recursivePathFinding(self, u, d, visited, path, paths):
        if u.islower():
            visited[u] += 1
        path.append(u)

        if u == d:
            paths.append(path)
        else:
            for i in self.graph[u]:
                if self.canIVisit(i, visited):
                    self.recursivePathFinding(i, d, visited, path, paths)

        path.pop()
        visited[u] -= 1

    def getAllPaths(self, start, end):
        visited = {vertex: 0 for vertex in self.V}
        current_path = []
        paths = []
        self.recursivePathFinding(start, end, visited, current_path, paths)
        print(len(paths))

    def canIVisit(self, i, visited):
        if visited[i] == 0:
            return True
        if visited[i] == 2:
            return False
        if visited[i] == 1:
            if i == 'start' or i == 'end':
                return False
            elif 2 in visited.values():
                return False
        return True

with open('Day12/input.txt') as f:
    data = [tuple(value.rstrip().split('-')) for value in f.readlines()]

vertices = set()

for a, b in data:
    vertices.add(a)
    vertices.add(b)

g = Graph(vertices)
print(vertices)
for edge in data:
    g.addEdge(*edge)

g.getAllPaths('start', 'end')
