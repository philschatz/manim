from manim import *

amp = 4
mu = 6
sig = 1.25
off=10
WHITE= "#fafafa"
GR1="#dcdcdc"
GR2="#979797"
BL="#464444"
GRUE= "#55c1b8"
def gaussian(x):
    return amp * np.exp((-1 / 2 * ((x - mu) / sig) ** 2)) + 3

class B(GraphScene):
    def construct(self):

        self.setup_axes()
        x_max = 5

        graph = self.get_graph(gaussian, x_min=-1, x_max=10).set_stroke(width=4.5*off).set_color(color=GR1)
        graph2 = self.get_graph(gaussian, x_min=-1, x_max=x_max).set_stroke(width=9*off).set_color(color=GR2)
        self.add(graph, graph2)


import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders  --disable_caching -s -r 400,400 -p -t --config_file '{project_path}/manim_settings.cfg' " + script_name)