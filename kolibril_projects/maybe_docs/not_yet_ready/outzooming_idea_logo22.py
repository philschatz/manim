from manim import *


class MovingCameraOnGraph(GraphScene, MovingCameraScene):
    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)
    def construct(self):
        self.camera_frame.scale(1.2)
        mobject= Mobject()
        def camera_zoom(mobj, dt):
            self.camera_frame.scale(.9975)
        self.add(mobject)
        mobject.add_updater(camera_zoom)

        self.setup_axes(animate=True)
        func_graph=self.get_graph(lambda x : np.sin(x))
        self.play(Write(func_graph))
        dot = Dot().move_to(self.coords_to_point(PI/2,1))
        dot2 = Dot().move_to(self.coords_to_point(5*PI/2,1))
        self.play(Write(VGroup(dot,dot2)))
        line = Line(dot.get_center(), dot2.get_center()).set_color(ORANGE)
        b1 = Brace(line,direction=UP)
        text = MathTex(r"\int_V\left(\nabla f\right)\mathrm{d}V = \oint_{S} f\,\mathrm d\vec S").next_to(b1,UP).shift(1.8*UP+RIGHT)
        self.play(Write(text))
        m0 = SmallDot().shift(UP)
        m1 = AnnotationDot().shift(LEFT)
        m2 = LabeledDot("ii").shift(RIGHT)
        m3 = LabeledDot(MathTex(r"\alpha").set_color(ORANGE)).shift(2*UP)
        m4 = CurvedArrow(ORIGIN, 2*LEFT).set_z_index(3)
        m5 = CurvedDoubleArrow(2*RIGHT+UP, 2*RIGHT).set_z_index(3)
        # self.add(dot,dot2,b1,text,m0,m1,m2,m3,m4,m5)
        banner= ManimBanner().scale(0.2)
        self.play(FadeOutAndShift(text,UP),banner.create(), lag_ratio = 0.5)
        mobject.remove_updater(camera_zoom)
        self.play(banner.expand())
        self.play(FadeOut(banner))
        self.wait()

import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim   --custom_folders -p   --disable_caching   -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)