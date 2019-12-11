import sys
from collections import defaultdict

tree = defaultdict(set)

for line in sys.stdin.readlines():
    x, y = line.strip().split(")")
    tree[x].add(y)


def count(node, depth):
    return depth + sum(count(child, depth + 1) for child in tree[node])


print(count("COM", 0))

graph = defaultdict(set)
for n, children in tree.items():
    graph[n].update(children)
    for c in children:
        graph[c].add(n)


def bfs(start, goal):
    visited = set()
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == goal:
            return path

        visited.add(node)
        for neighbour in graph[node]:
            if neighbour in visited:
                continue
            new_path = list(path)
            new_path.append(neighbour)
            queue.append(new_path)

    return visited


print(len(bfs("YOU", "SAN")) - 3)
