import pygame
from Node import Node
from Node import Path

import sys

class Interface:

    pygame.init()

    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Dijkstra")

    path = []
    nodes = []

    selected_node = None
    input_text = ""
    edge_weight = ""

    font = pygame.font.Font(None, 36)
    text = font.render(input_text, True, (0, 0, 0))

    running = True
    while running:
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Clic izquierdo
                    nodes.append(Node(input_text, x, y))
                    input_text = ""
                elif event.button == 3:  # Clic derecho
                    if not selected_node:
                        for node in nodes:
                            if abs(x - node.x) < 20 and abs(y - node.y) < 20:
                                selected_node = node
                                break
                    elif selected_node:
                        for node in nodes:
                            if abs(x - node.x) < 20 and abs(y - node.y) < 20 and node != selected_node:
                                if edge_weight.isdigit():
                                    path.append(Path(int(edge_weight), selected_node, node))
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
                            path.append(Path(int(edge_weight), selected_node, node))
                        selected_node = None
                        edge_weight = ""
                    else:
                        nodes.append(Node(input_text, x, y))
                        input_text = ""
                else:
                    if selected_node:
                        edge_weight += event.unicode
                    else:
                        input_text += event.unicode

        screen.fill((255, 255, 255))
        for node in nodes:
            node.draw(screen)
        for edge in path:
            edge.draw(screen)
        
        # Muestra el texto de entrada
        text = font.render(input_text, True, (0, 0, 0))
        screen.blit(text, (x, y))
        pygame.display.flip()
