from manim import *

amp = 4
mu = 6
sig = 1.2

def gaussian(x):
    return amp * np.exp((-1 / 2 * ((x - mu) / sig) ** 2)) + 5

class Plot3bGaussian(GraphScene):
    def construct(self):
        self.setup_axes()
        x_max = 5
        off=5
        do = Dot().set_color(BLACK).scale(off)
        graph = self.get_graph(gaussian, x_min=-1, x_max=10).set_stroke(width=4*off).set_color(color='#81B29A')
        graph2 = self.get_graph(gaussian, x_min=-1, x_max=x_max).set_stroke(width=9*off).set_color(color='#e07A5F')
        do.move_to(self.coords_to_point(x_max, gaussian(x_max)))
        self.add(graph, graph2, do)
        self.wait()


import os
from pathlib import Path
if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim   -c '#ece6e2' --custom_folders  --disable_caching -s -p  " + script_name)