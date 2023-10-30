import pygame
from Node import Node
from Node import Path

from Dijkstra import Graph


class Interface:
    def __init__(self, dimensions: tuple = (800, 600)):
        self.dimensions = dimensions

    def start(self):
        pygame.init()

        screen = pygame.display.set_mode(self.dimensions)
        pygame.display.set_caption("Dijkstra")

        path = []
        nodes = []
        path_nodes = []
        shortest_path = []
        graph = Graph()

        selected_node = None
        input_text = ""
        edge_weight = ""

        font = pygame.font.Font(None, 36)
        node_tag = font.render(input_text, True, (0, 0, 0))
        path_value = font.render(input_text, True, (0, 0, 0))

        running = True
        while running:
            x, y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Clic izquierdo
                        if nodes:
                            nodes.append(Node(input_text, x, y))
                        else:
                            nodes.append(Node(input_text, x, y, 0))
                        input_text = ""
                    elif event.button == 3:  # Clic derecho
                        if not selected_node:
                            for node in nodes:
                                if abs(x - node.x) < 20 and abs(y - node.y) < 20:
                                    selected_node = node
                                    break
                        elif selected_node:
                            for node in nodes:
                                if (
                                    abs(x - node.x) < 20
                                    and abs(y - node.y) < 20
                                    and node != selected_node
                                ):
                                    found_path = False
                                    if edge_weight == "":
                                        edge_weight = "1"
                                    new_path = Path(
                                        int(edge_weight), selected_node, node
                                    )
                                    for old_path in path:
                                        if old_path.compare(new_path):
                                            found_path = True
                                    if not found_path:
                                        path.append(new_path)
                                    selected_node = None
                                    edge_weight = ""

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if input_text:
                            input_text = input_text[:-1]
                        else:
                            edge_weight = edge_weight[:-1]
                    elif event.key == pygame.K_RETURN:
                        if selected_node:
                            if edge_weight.isdigit():
                                found_path = False
                                if edge_weight == "":
                                    edge_weight = "1"
                                new_path = Path(int(edge_weight), selected_node, node)
                                for old_path in path:
                                    if old_path.compare(new_path):
                                        found_path = True
                                if not found_path:
                                    path.append(new_path)
                            selected_node = None
                            edge_weight = ""
                        else:
                            nodes.append(Node(input_text, x, y))
                            input_text = ""
                    elif event.key == pygame.K_SPACE:
                        # TODO pass nodes and stuff
                        graph.pass_nodes(nodes)
                        path_nodes, shortest_path = graph.search_path()
                    else:
                        if selected_node:
                            edge_weight += event.unicode
                        else:
                            input_text += event.unicode

            screen.fill((255, 255, 255))
            # Muestra el texto de entrada
            node_tag = font.render(input_text, True, (0, 0, 0))
            path_value = font.render(edge_weight, True, (40, 40, 40))
            screen.blit(node_tag, (x, y))
            screen.blit(path_value, (x, y))
            for edge in path:
                edge.draw(screen)
            for edge in shortest_path:
                edge.draw(screen, (0, 255, 0), False)
            for node in nodes:
                node.draw(screen)

            pygame.display.flip()
