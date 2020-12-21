from manim import *

class Kinetics(Scene):
    def construct(self):
        GREY_BLACK = "#a9a9a9"
        SILVER = "#C0C0C0"
        silver_coord= [0,-2,0]
        silver_size= 0.15
        split_width=.1
        slit_annot= VGroup(Square(fill_opacity=0.3).set_color(BLACK), Square(0.4, fill_color=WHITE, fill_opacity=1, stroke_color=BLACK))
        slit_annot.apply_matrix(np.array([[0.5, 0.3,  0. ],
                                          [0 , 1.,  0. ],
                                          [0.,  0.,  1. ]]))
        slit_annot.rotate(angle=80*DEGREES,axis=LEFT)
        slit_annotA= slit_annot.copy()
        slit_annotA.move_to(silver_coord).shift(1.5*UP+2.5*LEFT)
        slit_annotA.title = Tex("Spalt A", color=BLACK).scale(0.5).next_to(slit_annotA,UP, buff=0.3*SMALL_BUFF)
        slit_annotB= slit_annot.copy()
        slit_annotB.move_to(silver_coord).shift(2.5*UP+2.5*LEFT)
        slit_annotB.title = Tex("Spalt B", color=BLACK).scale(0.5).next_to(slit_annotB,UP, buff=0.3*SMALL_BUFF)



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
        self.wait(9)

        radius = 3
        t_min = 0
        t_max1 = np.arcsin(2.5/ radius)

        def f1(x):
            radius = 3
            return [radius * np.cos(x) -radius,0.5+ radius * np.sin(x) , 0]
        # lenf1 = float(Curve([radius * cos(t) - radius, radius * sin(t)], (t, t_min, t_max1)).length)
        # print(lenf1)
        param_func1 = ParametricFunction(f1, t_min, t_max1).set_color(BLACK)
        self.add(param_func1)





import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim  --custom_folders -s --disable_caching  -p  -c 'WHITE' --config_file '{project_path}/manim_settings.cfg' " + script_name)