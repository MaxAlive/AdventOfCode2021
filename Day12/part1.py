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
            visited[u] = True
        path.append(u)

        if u == 'end':
            paths.append(path)
        else:
            for i in self.graph[u]:
                if visited[i] == False:
                    self.recursivePathFinding(i, d, visited, path, paths)

        path.pop()
        visited[u] = False

    def getAllPaths(self, start, end):
        visited = {vertex: False for vertex in self.V}
        current_path = []
        paths = []
        self.recursivePathFinding(start, end, visited, current_path, paths)
        print(len(paths))

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
