from manim import *

class Chain(Scene):
    def construct(self):
        dots = [Dot().shift(i*0.2*LEFT)for i in range(0,40)]
        VGroup(*dots).move_to(ORIGIN)
        valtracker= ValueTracker(0)
        def dot_updater(mobj):
            i= valtracker.get_value()
            mobj.set_color(RED)
            mobj.set_y(np.cos(mobj.get_x()+i))
        for dot in dots:
            dot.add_updater(dot_updater)
        self.add(*dots)
        self.play(valtracker.increment_value, 4, run_time=3)
import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim  --custom_folders  --disable_caching  -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)