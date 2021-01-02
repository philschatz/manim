from manim import *

class MovingAround(Scene):
    def construct(self):
        config.frame_rate=50
        square = Square(color=BLUE, fill_opacity=1)

        self.play(square.shift, LEFT)
        self.play(square.set_fill, ORANGE)
        self.play(square.scale, 0.3)
        self.play(square.rotate, 0.4)

import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim   --custom_folders  --disable_caching  -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)