from Node import Node
from Node import Path

import sys

path = []

nodes = []
visited = []

nodes.append(Node("A", 0))
nodes.append(Node("B"))
nodes.append(Node("C"))
nodes.append(Node("D"))
nodes.append(Node("E"))
nodes.append(Node("F"))
nodes.append(Node("G"))
nodes.append(Node("H"))

Path(10, nodes[0], nodes[1])
Path(2, nodes[0], nodes[2])
Path(1, nodes[1], nodes[7])
Path(5, nodes[2], nodes[3])
Path(3, nodes[3], nodes[4])
Path(4, nodes[4], nodes[5])
Path(1, nodes[5], nodes[6])
Path(2, nodes[6], nodes[7])

for node in nodes:
    if node.distance == 0:
        visited.append(node)
        node.visited = True

while True:
    for node in visited:
        for p in node.paths:
            p.check_distance()

    val = sys.maxsize
    flag_node = None
    flag_parent = None

    for node in visited:
        for n in node.neighbors:
            if n.distance < val and not n.visited:
                val = n.distance
                flag_node = n
                flag_parent = node

    visited.append(flag_node)
    flag_node.visited = True
    flag_node.add_parent(flag_parent)

    if not flag_node.neighbors:
        break

n = visited[-1]
path.append(n)
while n.parent:
    path.append(n.parent)
    n = n.parent

for node in path:
    print(node)

print("--------")

for node in visited:
    print(node)
