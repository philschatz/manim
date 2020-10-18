from manim import *


class ExampleTextAlignment(Scene):
    def construct(self):
        title=TextMobject("K-means clustering  and Logistic Regression").set_color(BLACK)
        self.add(title.to_edge(UP))
        t1=TextMobject("1. Measuring").set_color(BLACK).next_to(ORIGIN,direction=RIGHT,aligned_edge=UP)
        t2=TextMobject("2. Clustering").set_color(BLACK)
        t2.next_to(t1,direction=DOWN,aligned_edge=LEFT)
        t3=TextMobject("3. Regression").set_color(BLACK)
        t3.next_to(t2,direction=DOWN,aligned_edge=LEFT)
        t4=TextMobject("4. Prediction").set_color(BLACK)
        t4.next_to(t3,direction=DOWN,aligned_edge=LEFT)
        x=VGroup(t1,t2,t3,t4).scale_in_place(0.7)
        x.set_opacity(0.5)
        x.submobjects[1].set_opacity(1)
        self.add(x)

import os ; import sys
from pathlib import Path 
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders  --disable_caching -s -p -c 'WHITE' --config_file '{project_path}/manim_settings.cfg' " + script_name)