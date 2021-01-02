from manim import *
import matplotlib.pyplot as plt
class GraphExample(Scene):
    def construct(self):
        def f(x):
            return x**2
        l=Line(3*LEFT,5*RIGHT).shift(2*DOWN)
        self.add(MathTex("x=0").next_to(l.get_left(),UP))
        self.add(MathTex("x=1").next_to(l.get_right(),UP))
        self.add(l)
        fig, ax = plt.subplots()
        x= np.arange(0,100,1)
        ax.plot(x, f(x))
        fig.canvas.draw()
        img = ImageMobject(fig.canvas.buffer_rgba()).next_to(l,UP,buff=0)#.rotate(-20, [0.1, 1,0.1])
        plt.close(fig)
        img.apply_matrix(np.array([[0.5, 0.,  0. ],
                                [0.5, 1.,  0. ],
                                 [0.,  0.,  1. ]]).T)
        self.add(img)


import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim   --custom_folders -s  --disable_caching  -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)