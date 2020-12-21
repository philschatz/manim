from manim import *

class DDD(Scene):
    def construct(self):
        d1= Dot()
        d2= Dot().set_color(GREEN).scale(2)
        self.add(d1,d2)
        self.mobjects[0],self.mobjects[1] = self.mobjects[1], self.mobjects[0]

import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders  --disable_caching  -p  -s -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)