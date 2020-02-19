import ruckusCore
import random

classID5 = random.random()
class Day5(ruckusCore.Module):
    name = "Day 5"
    def __init__(self, app):
        super().__init__(app)
        self.classID = classID5

    def page(self, panel):
        return False

if __name__ == "__main__":
    app = ruckusCore.App([Day5])
    try:
        app.run()
    finally:
        app.game_engine.exit_program()