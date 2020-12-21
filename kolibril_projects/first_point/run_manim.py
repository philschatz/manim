from manim import *

class DDD(Scene):
    def construct(self):
        d1= Dot()
        self.add(d1)
        l1 = Line(LEFT,RIGHT)
        l2= VMobject()

        self.add(l1,l2)
        l2.add_updater(lambda x: x.become(Line(LEFT, d1.get_center()).set_color(ORANGE)))
        self.play(MoveAlongPath(d1,l1), rate_func= linear)
        
import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders  --disable_caching  -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)