from manim import *


class Example(Scene):
    def construct(self):
        def phi_func(t):
            phi = phi_max * np.sin(np.sqrt(g / l) * t) - 90*DEGREES
            return phi

        phi_max = 45 * DEGREES
        g = 9.81
        l = 1
        l_dis = 3
        t = ValueTracker(0)

        coordinate = [l_dis * np.cos(phi_func(t.get_value())),
                      l_dis * np.sin(phi_func(t.get_value())),
                      0]

        anchor = Dot()
        mass = LabeledDot(label= "1kg", point=coordinate).set_z(10)
        mass.add_updater(lambda x : x.move_to([l_dis * np.cos(phi_func(t.get_value())),
                                               l_dis * np.sin(phi_func(t.get_value())),
                                               0]))
        line = Line(anchor.get_center(), mass.get_center() , color= BLUE)
        line.add_updater(lambda x : x.become(Line(anchor.get_center(), mass.get_center(),color= BLUE)))
        self.add(anchor,mass, line, mass)
        self.play(t.increment_value, 1 ,rate_func = linear , run_time=2)


import os;
import sys
from pathlib import Path

if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(
        f"manim   --custom_folders -s --disable_caching -m  -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)
