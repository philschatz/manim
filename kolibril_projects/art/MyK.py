from manim import *

WHITE= "#fafafa"
GR1="#dcdcdc"
GR2="#979797"
BL="#464444"
GRUE= "#55c1b8"

class MyK(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        tex = Tex(r'$\mathbb{H}$}', tex_template=myTemplate).set_color(BLACK).rescale_to_fit(length=1.5*config.frame_height, dim =0)
        self.add(tex)
import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders  --disable_caching -s -r 400,400 -p -t --config_file '{project_path}/manim_settings.cfg' " + script_name)