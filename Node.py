import sys


class Node:
    pass


class Path:
    pass


class Node:
    def __init__(self, tag: str, distance: int = sys.maxsize) -> None:
        self.tag = tag
        self.distance = distance
        self.neighbors = []
        self.paths = []
        self.visited = False
        self.parent = None

    def update_distance(self, distance: int) -> None:
        self.distance = distance

    def add_neighbor(self, neighbor: Node) -> None:
        self.neighbors.append(neighbor)

    def add_path(self, path: Path) -> None:
        self.paths.append(path)

    def add_parent(self, parent: Node) -> None:
        self.parent = parent

    def __repr__(self) -> str:
        return f"Node {self.tag}: Distance {self.distance}, Visted {self.visited}"


class Path:
    def __init__(self, weight: int, start_node: Node, end_node: Node) -> None:
        self.weigth = weight
        self.start_node = start_node
        self.end_node = end_node
        self.start_node.add_neighbor(end_node)
        self.start_node.add_path(self)

    def check_distance(self) -> None:
        if self.weigth + self.start_node.distance < self.end_node.distance:
            self.end_node.distance = self.weigth + self.start_node.distance
