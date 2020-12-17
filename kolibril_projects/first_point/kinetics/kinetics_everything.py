from manim import *
from sympy.abc import t
from sympy import Curve
from sympy import sin, cos
class Kinetics(Scene):
    def construct(self):
        # PART A)
        GREY_BLACK = "#a9a9a9"
        SILVER = "#C0C0C0"
        dot_color = interpolate_color(SILVER, BLACK,0.1)

        silver_coord= [0,-2,0]
        silver_size= 0.15
        split_width=.1
        sq = Rectangle(height=6, width=2).set_color(BLACK)
        silv = Square(silver_size*2, fill_color=SILVER, stroke_color=SILVER, fill_opacity=1).move_to(silver_coord)
        silv.title = Tex("Silberquelle", color=BLACK).scale(0.5).next_to(silv,DOWN, buff=SMALL_BUFF)
        self.add(silv,silv.title)
        silver_holder = VGroup(Line([-1,-2,0],[0-silver_size,-2,0],color=BLACK),
                               Line([0+silver_size,-2,0],[1,-2,0], color=BLACK))
        self.add(sq)
        self.add(silver_holder)
        self.add(silv)
        slitA = VGroup(Line([-1,-0.5,0],[0-split_width,-0.5,0]),Line([0+split_width,-0.5,0],[1,-0.5,0])).set_color(BLACK)
        slitB = VGroup(Line([-1, 0.5,0],[0-split_width, 0.5,0]),Line([0+split_width, 0.5,0],[1, 0.5,0])).set_color(BLACK)
        self.add(slitA, slitB)
        self.bring_to_front(silv)
        self.add(DashedLine(silver_coord, 0.5*UP).set_color(dot_color))
        # PART B)

        r1 = 7
        r2= 8
        r3 = 9
        speed1=1.5
        speed2=1.8
        speed3=2.3
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





import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim  --custom_folders -m --disable_caching  -p  -c 'WHITE' --config_file '{project_path}/manim_settings.cfg' " + script_name)