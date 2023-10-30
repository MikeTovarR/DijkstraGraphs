from Node import Node
from Node import Path

import sys


class Graph:
    pass


class Graph:
    def __init__(self) -> Graph:
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
            # update weights
            for node in self.visited:
                for p in node.paths:
                    p.check_distance()
            val = sys.maxsize
            flag_node = None
            flag_parent = None

            # change the node to the neighboring node with least weight
            for node in self.visited:
                for n in node.neighbors:
                    if n.distance < val and not n.visited:
                        val = n.distance
                        flag_node = n
                        flag_parent = node

            # change the node to visited and add them to the list
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

        path.reverse()
        shortest = []
        for i in range(len(path) - 1):
            node_a = path[i]
            node_b = path[i + 1]
            for route in node_a.paths:
                comparable = Path(0, node_a, node_b)
                if route.compare(comparable):
                    shortest.append(comparable)
                    break

        return path, shortest
