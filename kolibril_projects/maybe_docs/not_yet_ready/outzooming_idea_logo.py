from manim import *


class MovingCameraOnGraph(GraphScene, MovingCameraScene):
    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)
    def construct(self):
        self.camera_frame.save_state()
        self.camera_frame.scale(0.2)
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        ds_m = MathTex(r"\mathbb{M}", z_index=20).scale(7)
        ds_m.shift(2.25*LEFT + 1.5*UP)
        circle = Circle(color=logo_green,
                        fill_opacity=1,
                        z_index=7)
        square = Square(color=logo_blue,
                        fill_opacity=1,
                        z_index=5)
        triangle = Triangle(color=logo_red,
                            fill_opacity=1,
                            z_index=3)
        circle.shift(LEFT)
        square.shift(UP)
        triangle.shift(RIGHT)
        vgroup = VGroup(triangle, square, circle, ds_m).move_to(ORIGIN).scale(0.2)
        self.add(vgroup)

        self.setup_axes(animate=False)
        func_graph=self.get_graph(lambda x : np.sin(x))
        dot = Dot().move_to(self.coords_to_point(PI/2,1))
        dot2 = Dot().move_to(self.coords_to_point(5*PI/2,1))
        line = Line(dot.get_center(), dot2.get_center()).set_color(ORANGE)
        b1 = Brace(line,direction=UP)
        text = MathTex("2\cdot \pi").next_to(b1,UP)
        m0 = SmallDot().shift(UP)
        m1 = AnnotationDot().shift(LEFT)
        m2 = LabeledDot("ii").shift(RIGHT)
        m3 = LabeledDot(MathTex(r"\alpha").set_color(ORANGE)).shift(2*UP)
        m4 = CurvedArrow(ORIGIN, 2*LEFT).set_z_index(3)
        m5 = CurvedDoubleArrow(2*RIGHT+UP, 2*RIGHT).set_z_index(3)
        self.add(func_graph)
        self.add(dot,dot2,b1,text,m0,m1,m2,m3,m4,m5)


        self.play(Restore(self.camera_frame), rate_function= linear, run_time=2)
        self.wait()

import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim   --custom_folders -p  --disable_caching   -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)