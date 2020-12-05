from manim import *

def lissajous_curve_func(t):
    return np.array((np.sin(3 * t), np.sin(4 * t)+2/3*PI, 0))

class PointWithTrace(Scene):
    def construct(self):
        path = VMobject()
        dot = Dot()
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        def update_path(path):
            previous_path = path.copy()
            self.remove(previous_path)
            path.add_points_as_corners([dot.get_center()])
            self.add(path)
        path.add_updater(update_path)
        func = ParametricFunction(lissajous_curve_func, t_max=TAU, fill_opacity=0).scale(3).move_to(ORIGIN)
        self.add(path)
        dot = AnnotationDot().scale(2)
        self.play(MoveAlongPath(dot, func), rate_func= linear , run_time=9)
        self.wait(0.1)

import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim  --custom_folders  --disable_caching  -p  -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)