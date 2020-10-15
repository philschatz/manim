from manim import *
import numpy as np
from active_projects.eop.reusables.histograms import *
##Histogram like this:
## 0   2    2     1 ....
#0   1    2    3    4 ...... 255...  256

class MinimalHist(Scene):
    def construct(self):
        Circle()
        values= [1,1,1,1,0,0,0,0,5,5,8,9,23,3,3,3,23,235,234,2,1,212,12,3,255]
        max=256
        val = np.histogram(values, bins=[i for i in np.arange(0, max+1)])
        hist= Image_Histogram(val[1], val[0], x_scale= 4/max)
        self.add(hist)
        self.wait(0.2)

from pathlib import Path
if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders  -s -p -c 'BLACK' --config_file '/home/jan-hendrik/.config/JetBrains/PyCharm2020.2/scratches/my_config.cfg' " + script )
