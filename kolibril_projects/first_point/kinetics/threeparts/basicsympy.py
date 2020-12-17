from manim import *
from sympy.abc import t
from sympy import Curve
from sympy import sin, cos

class ABCCC(Scene):
    def construct(self):
        line = Line(
            2 * UP + config.frame_width / 2 * LEFT,
            2 * UP + config.frame_width / 2 * RIGHT,
        )
        self.add(line)

        # start_here
        radius = 4
        t_min = 0
        t_max1 = np.arcsin(2 / radius)

        def f1(x):
            radius = 4
            return [radius * np.cos(x) - radius, radius * np.sin(x), 0]
        lenf1 = float(Curve((radius * cos(t) - radius, radius * sin(t)), (t, t_min, t_max1)).length)
        print(lenf1)
        param_func1 = ParametricFunction(f1, t_min, t_max1)
        dot1 = Dot()
        dot1.time = 0

        def func_updater1(mobj, dt):
            if mobj.timex % 10 == 0:
                mobj.submobjects.append(dot1.copy())
            for ob in mobj.submobjects:
                ob.time += 0.01*t_max1/lenf1
                ob.move_to(f1(ob.time))
                if ob.time >= t_max1:
                    mobj.submobjects.remove(ob)
            mobj.timex += 1

        param_func1.timex = 0
        param_func1.add_updater(func_updater1)
        self.add(param_func1)

        # # start_here2
        radius = 2.4
        t_min = 0
        t_max2 = np.arcsin(2 / radius)

        def f2(x):
            radius = 2.4

            return [radius * np.cos(x) - radius, radius * np.sin(x), 0]

        param_func2 = ParametricFunction(f2, t_min, t_max2)
        lenf2 = float(Curve((radius * cos(t) - radius, radius * sin(t)), (t, t_min, t_max2)).length)

        dot2 = Dot()
        dot2.time = 0

        def func_updater2(mobj, dt):
            if mobj.timex % 10 == 0:
                mobj.submobjects.append(dot2.copy())
            for ob in mobj.submobjects:
                ob.time += 0.01*t_max2/lenf2
                ob.move_to(f2(ob.time))
                if ob.time >= t_max2:
                    mobj.submobjects.remove(ob)
            mobj.timex += 1

        param_func2.timex = 0
        param_func2.add_updater(func_updater2)
        self.add(param_func2)
        self.wait(7)

    #
        # # start_here3
        # radius = 2.4
        # t_min = 0
        # t_max3 = np.arcsin(2 / radius)
        #
        # def f3(x):
        #     radius = 2.4
        #
        #     return [radius * np.cos(x) - radius, radius * np.sin(x), 0]
        #
        # param_func3 = ParametricFunction(f3, t_min, t_max3)
        # dot3 = Dot()
        # dot3.time = 0
        #
        # def func_updater3(mobj, dt):
        #     if mobj.timex % 3 == 0:
        #         mobj.submobjects.append(dot3.copy())
        #     for ob in mobj.submobjects:
        #         ob.time += 0.01
        #         ob.move_to(f3(ob.time))
        #         if ob.time >= t_max3:
        #             mobj.submobjects.remove(ob)
        #     mobj.timex += 1
        #
        # param_func3.timex = 0
        # param_func3.add_updater(func_updater3)
        # self.add(param_func3)
        #
        #
        #
        #
        #
        #
        # self.wait(5)
        #

import os
import sys
from pathlib import Path

if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(
        f"manim   --custom_folders -m  --disable_caching -p  -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' "
        + script_name
    )
