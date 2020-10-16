from manim import *

from manim import *
class Text3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES,theta=-45*DEGREES)
        text=TextMobject("This is a 3D text")
        self.add_fixed_in_frame_mobjects(text.to_corner(UL))
        self.add(axes)
        self.add(text)
        self.wait()

import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders  --disable_caching -s -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)