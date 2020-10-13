from manim import *


class InterpolationExample(Scene):
    def construct(self):
        dot = Dot()
        dot2 = Dot().shift(LEFT)
        dot3 = VMobject().interpolate(dot, dot2, alpha=0.4)
        self.add(dot, dot2, dot3)
        self.wait(2)


import os;
import sys
from pathlib import Path

if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(
        f"manim  -l --custom_folders  --disable_caching -s -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)
