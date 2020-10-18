from manim import *

class LotsOfImages(Scene):
    def construct(self):
        pixX,pixY=(200,200)
        im1 = [[(i+j)*5 for i in range(pixX)] for j in range(pixY)]
        im2 = np.random.randint(0, 255, size=(15, 15))
        im3=np.fromfunction(lambda i, j: 200*np.sin(j), (15, 15))
        a, b = np.meshgrid(np.linspace(-1,1,pixX), np.linspace(-1,1,pixY),sparse=False)
        im4 = 200*np.sqrt(a**2+b**2)
        imgs = [im1,im2,im3,im4]
        imgs_manim= []
        for val, i in enumerate(imgs):
            i = ImageMobject(np.uint8(i)).shift(5*LEFT)
            if val >= 1:
                i.next_to(imgs_manim[-1])
            imgs_manim.append(i)
        self.add(*imgs_manim)
        self.wait(2)

import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders  --disable_caching -s -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)