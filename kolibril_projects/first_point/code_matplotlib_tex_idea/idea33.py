from manim import *
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 150


class GraphExample(Scene):
    def construct(self):
        circ = Circle().set_color(YELLOW_C).shift(4*LEFT).scale(0.6)
        self.add(circ)
        squ = Square().shift(4*RIGHT).scale(0.6).set_fill("#87CEEB",1)
        img1= ImageMobjectFromCamera(self.camera)
        self.play(Transform(circ,squ),run_time=3)
        img2 = ImageMobjectFromCamera(self.camera)
        # self.remove(circ)
        self.add(img1.scale(0.5).to_corner(LEFT), img2.scale(0.5).to_corner(RIGHT))
        self.wait()


import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim   --custom_folders -s  --disable_caching  -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)