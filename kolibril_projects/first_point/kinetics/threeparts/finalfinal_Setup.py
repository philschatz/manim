from manim import *
from sympy.abc import t
from sympy import Curve
from sympy import sin, cos

class ABCCC(Scene):
    def construct(self):
        SILVER = "#C0C0C0"

        line = Line(
            3 * UP + config.frame_width / 2 * LEFT,
            3 * UP + config.frame_width / 2 * RIGHT,
        )
        self.add(line)

        r1 = 5
        r2= 6
        r3 = 7
        speed1=0.7
        speed2=1
        speed3=1.5
        dot_color = interpolate_color(SILVER, BLACK,0.1)
        # start_here 1
        radius = r1
        t_min = 0
        t_max1 = np.arcsin(2.5/ radius)
        def f1(x):
            radius = r1
            return [radius * np.cos(x) - radius,0.5+ radius * np.sin(x), 0]
        lenf1 = float(Curve([radius * cos(t) - radius, 0.5+radius * sin(t)], (t, t_min, t_max1)).length)
        print(lenf1)
        param_func1 = ParametricFunction(f1, t_min, t_max1 , stroke_color=dot_color, stroke_opacity=0.3 )
        dot1 = Dot(fill_color=dot_color).scale(0.5)
        dot1.time = 0

        def func_updater1(mobj, dt):
            if mobj.timex % 30 == 0:
                mobj.submobjects.append(dot1.copy())
            for ob in mobj.submobjects:
                ob.time += 0.01*t_max1/lenf1*speed1
                ob.move_to(f1(ob.time))
                if ob.time >= t_max1:
                    mobj.submobjects.remove(ob)
            mobj.timex += 1

        param_func1.timex = 0
        param_func1.add_updater(func_updater1)
        self.add(param_func1)

        # # start_here2
        radius = r2
        t_min = 0
        t_max2 = np.arcsin(2.5/radius)
        def f2(x):
            radius = r2
            return [radius * np.cos(x) - radius, 0.5+radius * np.sin(x), 0]
        param_func2 = ParametricFunction(f2, t_min, t_max2 , stroke_color=dot_color, stroke_opacity=0.3)
        lenf2 = float(Curve([radius * cos(t) - radius, 0.5 + radius * sin(t)], (t, t_min, t_max2)).length)
        dot2 = Dot(fill_color=dot_color).scale(0.5)
        dot2.time = 0
        def func_updater2(mobj, dt):
            if mobj.timex % 10 == 0:
                mobj.submobjects.append(dot2.copy())
            for ob in mobj.submobjects:
                ob.time += 0.01*t_max2/lenf2*speed2
                ob.move_to(f2(ob.time))
                if ob.time >= t_max2:
                    mobj.submobjects.remove(ob)
            mobj.timex += 1
        param_func2.timex = 0
        param_func2.add_updater(func_updater2)
        self.add(param_func2)

        # # start_here3
        radius = r3
        t_min = 0
        t_max3 = np.arcsin(2.5/radius)
        def f3(x):
            radius = r3
            return [radius * np.cos(x) - radius, 0.5+radius * np.sin(x), 0]
        param_func3 = ParametricFunction(f3, t_min, t_max3 , stroke_color=dot_color, stroke_opacity=0.3)
        lenf3 = float(Curve([radius * cos(t) - radius, 0.5 + radius * sin(t)], (t, t_min, t_max3)).length)
        dot3 = Dot(fill_color=dot_color).scale(0.5)
        dot3.time = 0
        def func_updater3(mobj, dt):
            if mobj.timex % 30 == 0:
                mobj.submobjects.append(dot3.copy())
            for ob in mobj.submobjects:
                ob.time += 0.01*t_max3/lenf3*speed3
                ob.move_to(f3(ob.time))
                if ob.time >= t_max3:
                    mobj.submobjects.remove(ob)
            mobj.timex += 1
        param_func3.timex = 0
        param_func3.add_updater(func_updater3)
        self.add(param_func3)
        self.wait(19)



import os
import sys
from pathlib import Path

if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(
        f"manim   --custom_folders -m  --disable_caching -p  -c 'WHITE' --config_file '{project_path}/manim_settings.cfg' "
        + script_name
    )
