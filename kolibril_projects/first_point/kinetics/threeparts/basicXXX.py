from manim import *

from manim import *
from sympy.abc import t
from sympy import Curve
from sympy import sin, cos


class ABC(Scene):
    def construct(self):
        line = Line(
            2 * UP + config.frame_width / 2 * LEFT,
            2 * UP + config.frame_width / 2 * RIGHT,
        )
        self.add(line)
        t_min = 0
        t_max = np.arcsin(2 / 3)

        def f(x):
            return [3 * np.cos(x) - 3, 3 * np.sin(x), 0]
        lenf = float(Curve((3 * cos(t) - 3, 3 * sin(t)), (t, t_min, t_max)).length)
        param_func = ParametricFunction(f, t_min, t_max)
        param_func.dots = []

        def dot_updater(mobj, dt):
            speed = 0.01
            if mobj.time >= t_max:
                mobj.time = 0
            mobj.move_to(f(mobj.time))
            mobj.time += speed

        for i in range(10):
            d = Dot().set_color(GREEN)
            d.time = i * 0.1
            d.add_updater(dot_updater)
            param_func.dots.append(d)

        self.add(param_func)
        self.add(*param_func.dots)
        self.wait(7)


import os
import sys
from pathlib import Path

if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(
        f"manim   --custom_folders  --disable_caching -p -l -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' "
        + script_name
    )
