from manim import *

class ABC(Scene):
    def construct(self):
        dot = Dot().set_color(GREEN)
        self.add(dot)
        self.wait(1)
        self.add_click_sound()
        self.wait()
import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders  --disable_caching -l -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)