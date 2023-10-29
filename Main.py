from Interface import Interface
import sys

dimensions = ()
if len(sys.argv) > 3:
    print("Unexepte number of arguments")
    exit(-1)
if len(sys.argv) == 3:
    dimensions = (int(sys.argv[1]), int(sys.argv[2]))
elif len(sys.argv) == 2:
    dimensions = (int(sys.argv[1]), int(sys.argv[1]))
elif len(sys.argv) == 1:
    dimensions = (800, 600)

screen = Interface(dimensions)

screen.start()
