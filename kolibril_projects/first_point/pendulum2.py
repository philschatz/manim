from manim import *


class Example(Scene):
    def construct(self):
        g = 9.81
        t = ValueTracker(0)


        anchor1 = Dot().set_color(BLUE)
        anchor2= Dot().set_color(RED)
        ancp1=[-2.5,2,0]
        ancp2= [2.5,0,0]
        anchor1.move_to(ancp1)
        anchor2.move_to(ancp2)

        def phi_func1(t):
            phi = phi_max1 * np.sin(np.sqrt(g / l1) * t +PI/2) - 90*DEGREES
            return phi

        phi_max1 = 20 * DEGREES
        l1 = 5
        l_dis1 = 5



        mass1 = LabeledDot(label= "1kg", point=[l_dis1 * np.cos(phi_func1(t.get_value())),
                                                l_dis1 * np.sin(phi_func1(t.get_value())),
                                                0]).shift(ancp1)
        mass1.add_updater(lambda x : x.move_to([l_dis1 * np.cos(phi_func1(t.get_value())),
                                               l_dis1 * np.sin(phi_func1(t.get_value())),
                                               0]).shift(ancp1))
        line1 = Line(anchor1.get_center(), mass1.get_center() , color= BLUE)
        line1.add_updater(lambda x : x.become(Line(anchor1.get_center(), mass1.get_center(),color= BLUE)))

        def phi_func2(t):
            phi = phi_max2 * np.sin(np.sqrt(g / l2) * t + PI/2) - 90*DEGREES
            return phi

        phi_max2 = 25.90919 * DEGREES
        l2 = 3
        l_dis2 = 3

        mass2 = LabeledDot(label= "1kg", point=[l_dis2 * np.cos(phi_func2(t.get_value())),
                                                l_dis2 * np.sin(phi_func2(t.get_value())),
                                                0]).shift(ancp2)
        mass2.add_updater(lambda x : x.move_to([l_dis2 * np.cos(phi_func2(t.get_value())),
                                                l_dis2 * np.sin(phi_func2(t.get_value())),
                                                0]).shift(ancp2))
        line2 = Line(anchor2.get_center(), mass2.get_center() , color= BLUE)
        line2.add_updater(lambda x : x.become(Line(anchor2.get_center(), mass2.get_center(),color= RED)))
        dashedline = DashedLine(LEFT*config.frame_width/2, RIGHT*config.frame_width/2).set_opacity(0.5)
        # dashedline.add_updater(lambda x: x.set_y(mass1.get_center()[1]))
        dashedline.set_y(mass1.get_center()[1])
        self.add(mass1,dashedline,anchor1,line1, mass1)
        self.add(mass2,anchor2,line2, mass2)
        self.play(t.increment_value, 12 ,rate_func = linear , run_time=10)
import os;
import sys
from pathlib import Path

if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(
        f"manim   --custom_folders  -p   --disable_caching   "
        f" -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)
