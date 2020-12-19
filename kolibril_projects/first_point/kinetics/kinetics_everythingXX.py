from manim import *
from sympy.abc import t
from sympy import Curve
from sympy import sin, cos
class Kinetics(ZoomedScene):
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.3,
            zoomed_display_height=2.3,
            zoomed_display_width=7,
            **kwargs)
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
        dashedl=DashedLine(silver_coord, 0.5*UP).set_color(dot_color)
        self.add(dashedl)
        # PART B)
        T1 = MathTex(r"\text{T}_{\text{kalt}} = 20^\circ C").set_color(BLACK)
        self.add(T1.scale(0.7).next_to(sq,LEFT).shift(2*DOWN))
        r1 = 5
        r2= 6
        r3 = 7
        speed1=0.7/2
        speed2=1/2
        speed3=1.5/2
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
                    ob.set_opacity(0)
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
                    ob.set_opacity(0)
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
            rem= False
            if mobj.timex % 30 == 0:
                mobj.submobjects.append(dot3.copy())
            for ob in mobj.submobjects:
                ob.time += 0.01*t_max3/lenf3*speed3
                ob.move_to(f3(ob.time))
                if ob.time >= t_max3:
                    ob.set_opacity(0)
            mobj.timex += 1
        param_func3.timex = 0
        param_func3.add_updater(func_updater3)
        self.add(param_func3)
        self.camera_frame.move_to(3*RIGHT)
        rot_anchor=5*RIGHT+2*DOWN
        self.add(Dot(color= RED, point=rot_anchor))
        self.add(CurvedArrow(rot_anchor+UR, rot_anchor+UL, color=BLACK).scale(0.3, about_point= rot_anchor).flip())

        kinetiker= VGroup(sq,silv,silver_holder,slitA,slitB,dashedl,param_func1,param_func2,param_func3).copy().scale(0.3).shift(rot_anchor+1.5*UP)
        self.add(kinetiker)
        self.tttime=0
        text1= Text("Sicht von mitrotierender Kamera").set_color(BLACK).scale(0.4).next_to(sq, DOWN)
        text2= Text("Sicht von außen").set_color(BLACK).scale(0.4).next_to(text1,RIGHT).set_x(5)
        bg=BackgroundRectangle(text2).set_fill(WHITE).set_opacity(0.7)
        self.add(text1)
        self.add(bg,text2)
        self.bring_to_front(sq)
        def update_mobj(mobj,dt):
            mobj.rotate(-0.5*dt, about_point=rot_anchor)
            self.tttime += dt
        kinetiker.add_updater(update_mobj)
        self.wait(2)

        self.activate_zooming(animate=False)
        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        frame = zoomed_camera.frame
        zoomed_display_frame = zoomed_display.display_frame
        frame.move_to(sq.get_top()+SMALL_BUFF*DOWN*3)
        frame.set_color(PURPLE)
        zoomed_display_frame.set_color(RED)
        zoomed_display.next_to(sq.get_top()+SMALL_BUFF*DOWN*3,RIGHT).set_x(rot_anchor[0])
        self.add(frame,zoomed_display)
        self.wait(25)
import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim  --custom_folders  --progress_bar False --disable_caching   -p  -c 'WHITE' --config_file '{project_path}/manim_settings.cfg' " + script_name)