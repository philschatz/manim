from manim import *
# class MovingCameraOnGraph(ZoomedScene,Scene):
#
#     def construct(self):
#         dot = Dot().set_color(GREEN)
#         sq = Circle(fill_opacity=1, radius=0.2).next_to(dot, RIGHT)
#         self.add(dot, sq)
#         self.wait(1)
#         self.activate_zooming(animate=False)
#         self.wait(1)
#         self.play(dot.shift, LEFT * 0.3)
#
#         self.play(self.zoomed_camera.frame.scale, 4)
#         self.play(self.zoomed_camera.frame.shift, 0.5 * DOWN)


class Kinetics( ZoomedScene):
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.3,
            zoomed_display_height=1,
            zoomed_display_width=6,
            **kwargs)
    def construct(self):
        dot= Dot()
        self.add(Dot())
        self.add(CurvedArrow(ORIGIN+UR, ORIGIN+UL).scale(0.4, about_point= ORIGIN).flip())
        self.add( dot)
        self.activate_zooming(animate=False)
        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        frame = zoomed_camera.frame
        zoomed_display_frame = zoomed_display.display_frame
        frame.move_to(dot)
        frame.set_color(PURPLE)
        zoomed_display_frame.set_color(RED)
        zoomed_display.shift(DOWN)
        self.add(frame,zoomed_display)
        T1 = MathTex(r"\text{T}_{\text{kalt}} = 20^\circ C").shift(DOWN)
        self.add(T1)
        self.wait()


import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim   --custom_folders -p   -l --disable_caching   -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)