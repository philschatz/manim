from manim import *

class Example(Scene):
    def construct(self):
        emmy= Text("Emmy Noether").to_edge(UP)
        img= ImageMobject("/home/jan-hendrik/projects/manim_resources/imgs_and_svgs/noeter.jpg").scale(0.5).next_to(emmy, DOWN)
        form = MathTex(r"\partial_\mu j^\mu = 0 ,\, j^\mu = \frac{\partial L}{\partial (\partial_{\mu} \phi)} \Delta \phi").next_to(img,DOWN)
        self.add(img,emmy)
        self.play(Write(form))
        self.wait()


import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim   --custom_folders  --disable_caching  -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)