
from manim import *

class Text(Scene):

    def construct(self):
        sq= Square()
        sq2= Square()
        sq2.next_to(sq,LEFT)
        sq3= Square()
        sq3.next_to(sq,RIGHT)
        circ = Circle().next_to(sq,DOWN)
        self.add(sq,sq2, sq3,circ)
        self.wait(1)
        self.play(*[FadeOut(x) for x in self.mobjects if x!= circ])
        self.wait()
        print("######")
        print( self.mobjects)

import os ; import sys
from pathlib import Path 
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders  --disable_caching -s -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)