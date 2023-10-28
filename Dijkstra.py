from Node import Node
from Node import Path

import sys


class Graph:
    def __init__(self) -> None:
        self.nodes = []
        self.visited = []

    def pass_nodes(self, nodes: list) -> None:
        self.nodes = nodes

    # Search a path until a node with no outgoing paths and return the shortest path
    def search_path(self) -> list:
        path = []
        for node in self.nodes:
            if node.distance == 0:
                self.visited.append(node)
                node.visited = True
        while True:
            for node in self.visited:
                for p in node.paths:
                    p.check_distance()
            val = sys.maxsize
            flag_node = None
            flag_parent = None

            for node in self.visited:
                for n in node.neighbors:
                    if n.distance < val and not n.visited:
                        val = n.distance
                        flag_node = n
                        flag_parent = node

            self.visited.append(flag_node)
            flag_node.visited = True
            flag_node.add_parent(flag_parent)

            if not flag_node.neighbors:
                break

        node = self.visited[-1]
        path.append(node)
        while node.parent:
            node = node.parent
            path.append(node)

        return path


# window = Interface()

# path = window.path

# nodes = window.nodes
# visited = []

# for node in nodes:
#     if node.distance == 0:
#         visited.append(node)
#         node.visited = True

# while True:
#     for node in visited:
#         for p in node.paths:
#             p.check_distance()

#     val = sys.maxsize
#     flag_node = None
#     flag_parent = None

#     for node in visited:
#         for n in node.neighbors:
#             if n.distance < val and not n.visited:
#                 val = n.distance
#                 flag_node = n
#                 flag_parent = node

#     visited.append(flag_node)
#     flag_node.visited = True
#     flag_node.add_parent(flag_parent)

#     if not flag_node.neighbors:
#         break

# n = visited[-1]
# path.append(n)
# while n.parent:
#     path.append(n.parent)
#     n = n.parent

# for node in path:
#     print(node)

# print("--------")

# for node in visited:
#     print(node)
