from manim import *
# this script will surely break, the only reason it is still here, is to be an inspiration when people want to try
# to use manim with music content
class music(Scene):

    def MuseMobject(self):
        FOLDER = "music_template/"
        FILE = "tex_template_music.tex"
        os.system("cd " + FOLDER + "&& latex -shell-escape " + FILE)
        temp1 = "out1.svg"
        os.system("cd " + FOLDER +" && eps2svg out-abc.eps " + temp1)
        temp2=  "out2.svg"
        os.system("cd " + FOLDER + "&& cairosvg "+ temp1 +" -f svg -o " + temp2)
        dat = FOLDER + temp2
        t = SVGMobject(dat) # or stroke_width = 2
        t.scale(2)
        self.add(t)
    def construct(self):
        self.MuseMobject()
        self.wait(2)

import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders  --disable_caching -s -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)