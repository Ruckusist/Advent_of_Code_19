import ruckusCore
import time
from timeit import default_timer as timer
from grams import din, test1, test2
from nextlib import MazeRunner
import threading
import multiprocessing

print("Starting it up.")

# global variables
logs = ["this","that","this is a super duper duper long string"]
avg_timer = []

# build map
maze = [x for x in test2.split("\n")]
maze.pop(0)
maze.pop(-1)

# build game engine
game = MazeRunner(maze, logs)

# build frontend
screen = ruckusCore.frontend.Window()
h = screen.screen_h
w = screen.screen_w
maze_h = len(maze)
maze_w = len(maze[0])
panel = screen.make_panel([h, w, 0, 0], "Maze")
panel[1].top()

# shortcut writing to the screen
showfps = lambda x: panel[0].addstr(88,88,"<FPS: {}>".format(x))
keystroke = lambda x: panel[0].addstr(h-2, w-9, "<K: {}>".format(x))
write = lambda x, y: panel[0].addstr(y, 1, x, screen.palette[2])

# game loop
loop = threading.Thread(target=game.run)
loop.start()
# loop = multiprocessing.Process(target=game.run)
# loop.start()
while True:
    try:
        # game timer
        start = timer()
        # =====================================>
        # APP GOES HERE
        # ???
        write(f"NEEDED KEYS: {[x for x in reversed(sorted(game.needed_keys))]}", 87)
        # =====================================>
        # write the log
        for index, log in enumerate(reversed(game.logs)):
            if index >= h: break
            panel[0].addstr(index+1, maze_w+2, f"{log[:31]}", screen.palette[3])
            
        # draw the map
        for h, lines in enumerate(game.maze):
            for w, chars in enumerate(lines):
                if "@" in chars: panel[0].addstr(h+1, w+1, "@", screen.palette[2])
                if "X" in chars: panel[0].addstr(h+1, w+1, ".", screen.palette[2])
                if "#" in chars: panel[0].addstr(h+1, w+1, "█", screen.palette[4])
                else: panel[0].addstr(h+1, w+1, f"{chars}", screen.palette[0])
        # refresh
        screen.refresh()
        time.sleep(.02)
        # calc fps
        avg_timer.append( timer() - start )
        if len(avg_timer)>10: avg_timer.pop(0)
        fps = sum(avg_timer)/len(avg_timer)
        showfps(f"{int(1/fps)}")
        
        # panel[0].addstr(h-1, w-12, f"FPS: {fps:.2f}")
        # panel[0].addstr(5, 5, f"FPS: {fps:.2f}")
        

    except KeyboardInterrupt:
        # loop.terminate()
        screen.end_safely()
        break
print("this is it.")