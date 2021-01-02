from manim import *


class Heugens(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        logo_green = "#87c2a5"
        pos1 = [-4,2,0]
        pos2 = [-4,1,0]
        pos3 = [-4,0,0]
        pos4 = [-4,-1,0]
        dot1 = Dot(pos1,color=BLACK)
        dot2 = Dot(pos2,color=BLACK)
        dot3 = Dot(pos3,color=BLACK)
        dot4 = Dot(pos4,color=BLACK)
        self.add(dot1,dot2,dot3,dot4)
        val_tracker = ValueTracker(0.4)
        circ1 = Arc(radius= 0.4).move_to(pos1)
        circ1.add_updater(lambda mobj: mobj.become(Circle(radius= val_tracker.get_value()).move_to(pos1)))
        circ2 = Circle(radius= 0.4).move_to(pos2)
        circ2.add_updater(lambda mobj: mobj.become(Circle(radius= val_tracker.get_value()).move_to(pos2)))
        circ3 = Circle(radius= 0.4).move_to(pos3)
        circ3.add_updater(lambda mobj: mobj.become(Circle(radius= val_tracker.get_value()).move_to(pos3)))
        circ4 = Circle(radius= 0.4).move_to(pos4)
        circ4.add_updater(lambda mobj: mobj.become(Circle(radius= val_tracker.get_value()).move_to(pos4)))
        self.wait(2)

import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders  --disable_caching -s -p --config_file '{project_path}/manim_settings.cfg' " + script_name)