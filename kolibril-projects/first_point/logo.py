from manim import *

class Test(GraphScene):
    def construct(self):
        self.add(Circle(fill_opacity = 0.3))


import os
from pathlib import Path
if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim   -t   --disable_caching -s -p  " + script_name)
