from manim import *

class No2(Scene):
    def construct(self):
        dot = SVGMobject("triangle.svg")
        dot.set_style(fill_opacity=0, stroke_width=2)
        self.add(dot)
        self.wait(1)
        
import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim   --custom_folders  --disable_caching -s -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)