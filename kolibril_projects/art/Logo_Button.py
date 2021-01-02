from manim import *

amp = 4
mu = 6
sig = 1.25
WHITE= "#fafafa"
GR1="#dcdcdc"
GR2="#979797"
BL="#464444"
GRUE= "#55c1b8"
def gaussian(x):
    return amp * np.exp((-1 / 2 * ((x - mu) / sig) ** 2)) + 5

class Button(GraphScene):
    def construct(self):
        d1= Dot().set_color(GRUE).scale(15)
        d2 = d1.copy().next_to(d1, LEFT, buff=1.7)
        d3 = d1.copy().next_to(d1, RIGHT, buff=1.7)
        li = Line(d2.get_center(),d3.get_center(),stroke_width=140 , z_index=-10).set_color(GR1)
        self.add(d1,d2,d3,li)

import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders  --disable_caching -s -r 400,400 -p -t --config_file '{project_path}/manim_settings.cfg' " + script_name)