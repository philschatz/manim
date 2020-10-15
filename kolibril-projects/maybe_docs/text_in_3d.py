from manim import *


class Text3D3(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES,theta=-45*DEGREES)
        text=TextMobject("This is a 3D text")
        self.add_fixed_in_frame_mobjects(text)
        self.add(axes)
        self.add(text)
        self.wait()
