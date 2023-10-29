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
        if not self.visited:
            pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 20)
        else:
            pygame.draw.circle(screen, (0, 0, 255), (self.x, self.y), 20)
        font = pygame.font.Font("Arial.ttf", 36)
        text = font.render(self.tag, True, (0, 0, 0))
        screen.blit(text, (self.x - 10, self.y - 20))
        weight = None
        if self.distance != sys.maxsize:
            weight = font.render(str(self.distance), True, (0, 0, 0))
        else:
            weight = font.render("∞", True, (0, 0, 0))
        screen.blit(weight, (self.x, self.y - 50))


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

    def draw(self, screen, color=(0, 0, 255), show_weight: bool = True):
        pygame.draw.line(
            screen,
            color,
            (self.start_node.x, self.start_node.y),
            (self.end_node.x, self.end_node.y),
            5,
        )
        font = pygame.font.Font(None, 20)
        text = font.render(str(self.weigth), True, (0, 0, 0))
        x = (self.start_node.x + self.end_node.x) / 2
        y = (self.start_node.y + self.end_node.y) / 2
        if show_weight:
            screen.blit(text, (x, y))

    # Checks if path includes both end points of comparable path
    def compare(self, path: Path) -> bool:
        if (path.start_node == self.start_node and path.end_node == self.end_node) or (
            path.start_node == self.end_node and path.end_node == self.start_node
        ):
            return True
        return False

    def __repr__(self) -> str:
        return f"Node {self.start_node.tag} to node {self.end_node.tag}"
