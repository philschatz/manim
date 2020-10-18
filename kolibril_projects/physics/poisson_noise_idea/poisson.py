from kolibril_projects.first_point.histo_3b1b import Image_Histogram
from manim import *


class poisson_and_snr(Scene):
    def construct(self):
        img= np.ones((32,32))+33
        img= np.random.poisson(img, (32,32) )

        max = 256
        val = np.histogram(img, bins=[i for i in np.arange(0, max + 1)])
        hist = Image_Histogram(val[1], val[0], x_scale=4 / max, y_scale=3/val[0].max())
        self.add(hist)
        self.wait(2)

import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders  --disable_caching -s -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)