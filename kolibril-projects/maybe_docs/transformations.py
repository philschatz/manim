from manim import *

class Shapes(Scene):
    CONFIG ={
        "color": BLUE
    }

    def construct(self):
        print("Start")

        dot = Dot()
        line=Line(np.array([3,0,0]),np.array([5,0,0]))
        self.add(line)
        dot2= dot.copy().shift(RIGHT)
        circle = Circle(radius= 1, color=BLUE)
        self.add(dot)
        self.play(GrowFromCenter(circle))
        self.play(Transform(dot,dot2))
        self.play(MoveAlongPath(dot,circle), run_time= 1, rate_func=linear)
        self.play(Rotating(dot,about_point= np.array((2, 0, 0.))))

import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders  --disable_caching  -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)