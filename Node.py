import sys
import pygame

class Node:
    pass


class Path:
    pass


class Node:
    def __init__(self, tag: str, x, y, distance: int = sys.maxsize) -> None:
        self.tag = tag
        self.distance = distance
        self.neighbors = []
        self.paths = []
        self.visited = False
        self.parent = None
        self.x = x
        self.y = y

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

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 20)
        font = pygame.font.Font(None, 36)
        text = font.render(self.tag, True, (0, 0, 0))
        screen.blit(text, (self.x - 10, self.y - 20))


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
    
    def draw(self, screen):
        pygame.draw.line(screen, (0, 0, 255), (self.start_node.x, self.start_node.y), (self.end_node.x, self.end_node.y), 5)
        font = pygame.font.Font(None, 20)
        text = font.render(str(self.weigth), True, (0, 0, 0))
        x = (self.start_node.x + self.end_node.x) / 2
        y = (self.start_node.y + self.end_node.y) / 2
        screen.blit(text, (x, y))
