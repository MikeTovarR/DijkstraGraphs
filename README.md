# DijkstraGraphs

_Made by Miguel Tovar and Carlos Velez_

---

A python project that shows the functionality and output of Dijkstra algorithm in a GUI

built in pygame. To run the program the user must have pygame installed.

```
pip install pygame
```

The user will be able to click the main screen of the app to add path nodes and create paths between
them. At the end the program will show the user the shortest path between the first node and to the node with no outgoing paths.

## Instructions

To run the code go to the terminal and run the command:

    py Main.py [width] [height]

Where width and height are optional parameters to change the size of the pygame screen. If only one argument is passed
then the screen is shown as an argument\*argument square.

Once in the app screen the user can enter text to change the input for the next tag or weight.

- **Left Click**: Create graph node
- **Right Click**: Create a path between nodes. Click from start node to end node
- **Space**: Search for paths
