from manim import *


class ShapesExampe(Scene):
    CONFIG ={
        "color": [DARK_BLUE , DARK_BROWN, BLUE_E, BLUE_D, BLUE_A, TEAL_B, GREEN_B, YELLOW_E],
        "radius": [1+rad*0.1 for rad,col in enumerate("color")]
    }
    def construct(self):
        cirlce_Subset=VGroup()
        k= 1
        cirlce_Subset.add(*[Circle(radius=rad+k,stroke_width=10, color = col)
                     for rad,col in zip(self.radius,self.color)])


        self.add(cirlce_Subset)
        self.wait(2)


import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders  --disable_caching -s -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)