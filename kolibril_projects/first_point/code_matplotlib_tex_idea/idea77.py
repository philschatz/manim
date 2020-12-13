from manim import *
import matplotlib.pyplot as plt
class GraphExample(Scene):
    def construct(self):
        sq= Square(fill_opacity=0.3)
        sq.apply_matrix(np.array([[0.5, 0.,  0. ],
                                  [0.5, 1.,  0. ],
                                 [0.,  0.,  1. ]]))
        img = ImageMobject("noeter.jpg").scale(0.3)
        img = ImageMobject
        self.add(img)
        self.add(sq)





import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim   --custom_folders -s  --disable_caching  -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)