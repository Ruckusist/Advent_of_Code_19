from star import Node
import re

class MazeRunner(object):
    def __init__(self, maze, logs):
        self.collected_keys = []
        self.needed_keys = []
        self.step_counter = 0
        self.path_order = []
        self.cur_position = (0,0)
        self.logs = logs
        self.maze = maze
        self.is_lowercase = lambda x: re.match(r"[a-z]", x)
        self.is_uppercase = lambda x: re.match(r"[A-Z]", x)

    def check_for_all_keys(self):
        for h, line in enumerate(self.maze):
            for w, char in enumerate(line):
                if self.is_lowercase(char):
                    self.needed_keys.append(char)
        self.logs.append("finished updating needed keys.")

    def find_door(self):
        self.get_position()
        start_node = Node(None, self.cur_position)
        start_node.g = start_node.h = start_node.f = 0
        open_list = []
        closed_list = []

        open_list.append(start_node)
        current_index = 0

        for h, line in enumerate(self.maze):
            for w, char in enumerate(line):
                pass

    def find_key(self): return
    def get_position(self, verbose=False): 
        for h, line in enumerate(self.maze):
            for w, char in enumerate(line):
                if "@" in char: 
                    self.cur_position = (h,w)
                    if verbose: print(f"\tgot position --> {self.cur_position}.")
                    return

    def move_to_position(self): return
    def run(self):
        self.check_for_all_keys()
        self.get_position()
        self.logs.append(f"Got position of {self.cur_position}")
        return

    def print(self):
        for i in self.maze:
            print(i)

if __name__ == "__main__":
    app = MazeRunner([], [])
    app.print()
    app.run()