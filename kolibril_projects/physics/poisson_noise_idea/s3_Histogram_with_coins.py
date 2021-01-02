from kolibril_projects.physics.poisson_noise_idea.histo_3b1b import Image_Histogram
from manim import *


class Coin_Fipping(Scene):
    def construct(self):
        ##histogram coins
        coins_in_array = np.load("coins_in_array.npy")
        coins_per_draw=20
        amount_of_draw=100
        FLIP10_ALL = [coins_in_array[0 + k:coins_per_draw + k]
                      for k in np.arange(0, amount_of_draw*coins_per_draw,coins_per_draw)]
        FLIP10_HEADS = np.array([sum(flip10) for flip10 in FLIP10_ALL])
        val = []
        for k,value in enumerate(FLIP10_HEADS):
            elements=FLIP10_HEADS[0:k+1]
            print(elements)
            val.append(np.histogram(elements, bins=[i for i in np.arange(0, coins_per_draw)]))
        x = None
        for draw_count, [hist, bin_edges] in enumerate(val,1):
            y_scale= 1
            if hist.max()>3:
                y_scale=3/hist.max()
            grade_hist = Histogram( bin_edges, hist, mode="posts",
                                    x_scale=12/coins_per_draw, y_scale= y_scale,x_labels= "mids+shift" )
            NEW_ORIGIN=  DOWN*3+LEFT*5-grade_hist.get_lower_left_point()
            grade_hist.move_to(NEW_ORIGIN)
            if x== None:
                x=grade_hist
            a=TextMobject("Amount of coins that show head in ", str(coins_per_draw) ," coins per draw")
            a.set_color_by_tex(str(coins_per_draw), GREEN)
            b=TextMobject("Number of draw: " , str(draw_count))
            b.set_color_by_tex(str(draw_count), BLUE)
            a.next_to(4*UP, DOWN)
            b.next_to(a,DOWN)
            self.clear()
            self.add(grade_hist, a,b)
            print(hist)
            self.wait(0.2)


import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders  --disable_caching -s -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)












