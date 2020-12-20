from manim import *

from manim import *
from sympy.abc import t
from sympy import Curve
from sympy import sin, cos


from manim import *

class Test(Scene):
    def construct(self):
        dot = Dot().set_color(GREEN)
        self.add(dot)
        self.wait(30)

import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim   --custom_folders  --disable_caching -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)

