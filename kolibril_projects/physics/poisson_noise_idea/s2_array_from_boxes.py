from manim import *


class Array_from_boxes(Scene):
    def construct(self):
        original_square= Square(fill_opacity=1)
        original_square.to_corner(RIGHT)
        PIXELS=64
        square_ALL= [Square(fill_opacity=1 , side_length=0.14) for i in range(0,PIXELS)]
        j=0
        for  i,square_to_move in enumerate(square_ALL):
            if i%np.sqrt(PIXELS)==0:
                j+=1
            k= i-j*np.sqrt(PIXELS)
            square_to_move.move_to(4*UP+(LEFT*k+j*DOWN)*0.2)


        term = VGroup(*[square for square in square_ALL])
        self.add(original_square)
        term.to_corner(RIGHT+UP)
        self.play(Transform(original_square, term), lag_ratio=0.2, run_time=4)
        t2= original_square.copy()
        t2.rotate(-20, [0, 1, 0.05])
        self.play(Transform(original_square,t2))

        self.wait(2)

import os ; import sys
from pathlib import Path 
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders  --disable_caching -s -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)







