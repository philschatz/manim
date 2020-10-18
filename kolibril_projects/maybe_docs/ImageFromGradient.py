from manim import *


class ImageFromGradient(Scene):
    def construct(self):
        print("Start")
        n=256
        img_A= np.uint8([[i for i in range(0,256)]  for j in range(0,256)])
        img1= ImageMobject(img_A).scale(2)
        img1.next_to(ORIGIN,LEFT, SMALL_BUFF)
        self.add(img1)
        self.wait(1)


import os;
import sys
from pathlib import Path

if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(
        f"manim  -l --custom_folders  --disable_caching -s -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)
