import random, threading, time, copy
import ruckusCore
import int_comp
"""
Guesses : 277 and 278, 279 are all wrong. and too low... but seem too high by my count.
it says there are 283 number 1 tiles out there... but there are at least 3 dead ends.
so the correct answer is 280.
"""

classID = random.random()
class Santa(ruckusCore.Module):
    name = "SantaLike"
    def __init__(self, app):
        super().__init__(app)
        self.classID = classID
        self.repair = int_comp.Repair()
        self.bot_on = False
        self.position_2 = [0,0]
        # self.checking = [self.position]
        self.path = []
        self.status1 = "Press Space to Let Santa Play"
        self.status2 = ""
        self.status3 = f"Position 2: ({self.position_2[0]}, {self.position_2[1]})"

    def unique_actions(self): return int(len(set(tuple(x) for x in self.path)))

    def end_safely(self):
        self.bot_on = False

    def page(self, panel=None) -> False:
        max_w = int(self.frontend.winright_dims[1])-2
        max_h = int(self.frontend.winright_dims[0])-2

        index = 1
        counter = 0

        gameboard = self.repair.gameboard
        position = self.repair.position

        mess1 = f"Gameboard = ({len(gameboard)}, {len(gameboard[0])})"
        mess2 = f"Position = ({position[0]}, {position[1]})"
        panel.addstr(index, 1, f"+ SantaLike + | {mess1} | {mess2}"[:max_w-2]); index += 1
        panel.addstr(index, 1, f"#"*max_w); index += 1
        
        for i_h, h in enumerate(range(position[0]-15, position[0]+25)):
            if i_h >= 37: continue
            counter += 1
            for i_w, w in enumerate(range(position[1]-int(max_w/2)+9, position[1]+int(max_w/2)+9)):
                if i_w >= max_w - 4: continue
                data = gameboard[h][w]
                if position == [h, w]: 
                    icon = 'X'
                    color = self.frontend.palette[6]
                else:
                    if   data == 0: icon = "█"; color = self.frontend.palette[5]
                    elif data == 1: icon = "▓"; color = self.frontend.palette[3]
                    elif data == 2: icon = "X"; color = self.frontend.palette[3]
                    elif data == 9: icon = " "; color = self.frontend.palette[0]
                    elif data == 8: icon = "▓"; color = self.frontend.palette[2]
                    elif data == 7: icon = "X"; color = self.frontend.palette[7]
                    else:
                        icon = '?'; color = self.frontend.palette[1]
                panel.addstr(i_h+index, i_w+3, str(icon), color)
        index += counter
        panel.addstr(index, 1, f"#"*max_w); index += 1
        panel.addstr(index, 1, f"{self.status1}", self.frontend.palette[3]); index += 1
        panel.addstr(index, 1, f"{self.status2}", self.frontend.palette[3]); index += 1
        panel.addstr(index, 1, f"{self.status3}", self.frontend.palette[3]); index += 1
        panel.addstr(index, 1, f"Found it yet?? {self.repair.found_it} | Path Len: {self.unique_actions()}", self.frontend.palette[3]); index += 1

    @ruckusCore.callback(classID, ruckusCore.Keys.ENTER)
    def on_enter(self, *args, **kwargs):
        self.repair.once()

    @ruckusCore.callback(classID, ruckusCore.Keys.A)
    def on_left(self, *args, **kwargs):
        self.repair.input = 3
        self.repair.once()

    @ruckusCore.callback(classID, ruckusCore.Keys.D)
    def on_right(self, *args, **kwargs):
        self.repair.input = 4
        self.repair.once()

    @ruckusCore.callback(classID, ruckusCore.Keys.W)
    def on_up(self, *args, **kwargs):
        self.repair.input = 1
        self.repair.once()

    @ruckusCore.callback(classID, ruckusCore.Keys.S)
    def on_down(self, *args, **kwargs):
        self.repair.input = 2
        self.repair.once()

    @ruckusCore.callback(classID, 112)
    def on_save(self, *args, **kwargs):
        #with open('logs/data.txt', 'w') as t:
        #    for x in self.repair.gameboard:
        #        t.write("".join(str(x)))
        counter = 0
        for i in self.repair.gameboard:
            for x in i:
                if x == 1:
                    counter += 1
        self.status2 = f"button pressed | counter = {counter}"

    @ruckusCore.callback(classID, ruckusCore.Keys.SPACE)
    def on_space(self, *args, **kwargs):
        if self.bot_on: 
            self.bot_on = False
        else: 
            self.bot_on = True
            threading.Thread(target=self.CRAZY_BOT_TIME).start()

    def CRAZY_BOT_TIME(self):
        while True:
            if not self.bot_on: break
            # if self.repair.found_it: break
            self.status1 = "Press Space to Stop Santa (running...)"
            if False:  # let the Mad Santa Play
                self.repair.input = random.randint(1,4)
                self.repair.once()

            if False:  # let the Genius Santa Play --> Part 1
                while True:
                    if self.repair.found_it: break
                    if not self.bot_on: break
                    current = self.repair.surroundings()

                    for i, e in enumerate(current):  # Do the 2's First
                        if int(self.repair.translate([e])[0]) == 2:
                            self.bot_on = False
                            break

                    if not self.bot_on: break

                    for i, e in enumerate(current):  # Do the 9's Second
                        self.status1 = f"{i+1} | {self.repair.direct(i+1)} | {self.repair.translate([e])[0]} --> Checking"
                        # time.sleep(.1)
                        if int(self.repair.translate([e])[0]) == 9:
                            self.status2 = f"GOT AN Unknown Direction! Checking it out!"
                            # time.sleep(.1)
                            if i+1 == 1:
                                reverse = 2
                            if i+1 == 2:
                                reverse = 1
                            if i+1 == 3:
                                reverse = 4
                            if i+1 == 4:
                                reverse = 3
                            self.repair.input = i+1
                            self.repair.once()
                            # time.sleep(.1)
                            if self.repair.action == 1:
                                self.status2 = f"GOT A OPEN PATH! but we need to go back..."
                                self.repair.input = reverse
                                self.repair.once()
                                # time.sleep(.1)
                            # time.sleep(.1)
                    
                    self.status2 = "Finished Checking the 9's"
                    self.path.append(self.repair.position)
                    self.status2 = "Now Checking the 1's"

                    available_tiles = []
                    for i, tile in enumerate(current):  # Then the 1's
                        self.status1 = f"{i+1} | {self.repair.direct(i+1)} | {self.repair.translate([tile])[0]} --> Checking"
                        if int(self.repair.translate([tile])[0]) == 1:
                            if tile not in self.path:
                                available_tiles.append(tile)

                    self.status2 = "Finished Checking the 1's"

                    if len(available_tiles) == 1:
                        x = current.index(available_tiles[0])+1
                        self.repair.input = x
                        self.status2 = f"Picked a New Direction --> {x} --> starting again"
                        self.repair.once()
                        time.sleep(.01)

                    if len(available_tiles) == 0:
                        if self.repair.gameboard[self.repair.position[0]][self.repair.position[1]] == 2:
                            self.bot_on = False
                            break
                        self.repair.gameboard[self.repair.position[0]][self.repair.position[1]] = 8
                        self.path.pop()
                        self.path.pop()
                        for i, tile in enumerate(current):
                            if int(self.repair.translate([tile])[0]) == 1:
                                self.repair.input = i + 1
                                self.status2 = f"Picked a New Direction --> {i+1} --> starting again"
                                self.repair.once()
                                time.sleep(.01)
                                break
                        # self.bot_on = False
                        # break

                    if len(available_tiles) > 1:
                        x = current.index(available_tiles[-1])+1
                        self.repair.input = x
                        self.status2 = f"Picked a New Direction --> {x} --> starting again"
                        self.repair.once()
                        time.sleep(.01)
            
            if True:  # let the Genius Santa Play
                while True:
                    if not self.bot_on: break
                    current = self.repair.surroundings()
                    
                    if not self.bot_on: break

                    for i, e in enumerate(current):  # Do the 9's Second
                        self.status1 = f"{i+1} | {self.repair.direct(i+1)} | {self.repair.translate([e])[0]} --> Checking"
                        # time.sleep(.1)
                        if int(self.repair.translate([e])[0]) == 9:
                            self.status2 = f"GOT AN Unknown Direction! Checking it out!"
                            # time.sleep(.1)
                            if i+1 == 1:
                                reverse = 2
                            if i+1 == 2:
                                reverse = 1
                            if i+1 == 3:
                                reverse = 4
                            if i+1 == 4:
                                reverse = 3
                            self.repair.input = i+1
                            self.repair.once()
                            # time.sleep(.1)
                            if self.repair.action == 1:
                                self.status2 = f"GOT A OPEN PATH! but we need to go back..."
                                self.repair.input = reverse
                                self.repair.once()
                                # time.sleep(.1)
                            # time.sleep(.1)
                    
                    self.status2 = "Finished Checking the 9's"
                    self.path.append(self.repair.position)
                    self.status2 = "Now Checking the 1's"

                    available_tiles = []
                    for i, tile in enumerate(current):  # Then the 1's
                        self.status1 = f"{i+1} | {self.repair.direct(i+1)} | {self.repair.translate([tile])[0]} --> Checking"
                        if int(self.repair.translate([tile])[0]) == 1:
                            if tile not in self.path:
                                available_tiles.append(tile)

                    self.status2 = "Finished Checking the 1's"

                    if self.repair.gameboard[self.repair.position[0]][self.repair.position[1]] == 2:
                        self.repair.gameboard[self.repair.position[0]][self.repair.position[1]] = 7
                        self.position_2 = copy.copy(self.repair.position)
                    
                    if len(available_tiles) == 1:
                        x = current.index(available_tiles[0])+1
                        self.repair.input = x
                        self.status2 = f"Picked a New Direction --> {x} --> starting again"
                        self.repair.once()
                        time.sleep(.01)

                    if len(available_tiles) == 0:
                        # if self.repair.gameboard[self.repair.position[0]][self.repair.position[1]] == 2:
                        #     self.repair.gameboard[self.repair.position[0]][self.repair.position[1]] = 7
                        #     self.position_2 = copy.copy(self.repair.position)
                        self.repair.gameboard[self.repair.position[0]][self.repair.position[1]] = 8

                        for i, tile in enumerate(current):
                            if int(self.repair.translate([tile])[0]) == 1:
                                self.repair.input = i + 1
                                self.status2 = f"Picked a New Direction --> {i+1} --> starting again"
                                self.repair.once()
                                time.sleep(.01)

                    if len(available_tiles) > 1:
                        x = current.index(available_tiles[-1])+1
                        self.repair.input = x
                        self.status2 = f"Picked a New Direction --> {x} --> starting again"
                        self.repair.once()
                        time.sleep(.01)

        self.status1 = "Press Space to Let Santa Play"
        self.status2 = ""


app = ruckusCore.App([Santa])
app.run()