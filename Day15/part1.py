from queue import PriorityQueue
from collections import defaultdict

def heuristic(point1, point2):
    (x1, y1) = point1
    (x2, y2) = point2
    return abs(x1 - x2) + abs(y1 - y2)

def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = defaultdict(int)
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            break
        
        for next in graph.neighbors[current]:
            new_cost = cost_so_far[current] + graph.weights[next]
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(next, goal)
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far
    

class GridWithWeights():
    def __init__(self, input_data):
        self.neighbors = defaultdict(set)
        self.weights = defaultdict(int)
        self.height = len(input_data)
        self.width = len(input_data[0])
        self.generate(input_data)

    def generate(self, data):
        for x in range(self.width):
            for y in range(self.height):
                self.weights[(x, y)] = int(data[y][x])
                if x+1 < self.width:
                    self.neighbors[(x, y)].add((x+1, y))
                    self.neighbors[(x+1, y)].add((x, y))
                if y+1 < self.height:
                    self.neighbors[(x, y)].add((x, y+1))
                    self.neighbors[(x, y+1)].add((x, y))

with open('Day15/input.txt') as f:
    data = [line.rstrip() for line in f.readlines()]

graph = GridWithWeights(data)
came_from, cost_so_far = a_star_search(graph, (0,0), (99,99))

print(cost_so_far[99,99])
