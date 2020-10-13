from manim import *
import matplotlib.pyplot as plt


def get_image_plot(t, dispersion):

    x = np.linspace(-25, 100, 10001)

    def g(x, t):
        omega = 1
        k = 0.5
        return 7*np.cos(k*x-omega*t)
    fig, ax = plt.subplots(figsize=(14, 3))
    ax.set_xlim(-15, 100)
    ax.set_ylim(-10, 10)
    ax.annotate(r'x in [m]',
                xy=(1, 0), xycoords='axes fraction',
                xytext=(-20, 20), textcoords='offset pixels',
                horizontalalignment='right',
                verticalalignment='bottom',
                fontsize=20)
    ax.plot(x, g(x, t))
    fig.canvas.draw()
    img = ImageMobject(fig.canvas.buffer_rgba())
    plt.close("all")
    return img


class WOnlyCos(Scene):

    def construct(self):
        t1 = 1
        t2 = 20

        tr_time1 = ValueTracker(t1)
        image1 = get_image_plot(tr_time1.get_value(), dispersion="const")

        def update_image1(mob):
            new_mob = get_image_plot(
                tr_time1.get_value(), dispersion="const"
            )
            new_mob.move_to(mob.get_center())
            mob.become(new_mob)

        image1.add_updater(update_image1)

        self.add(image1)
        image1.to_corner(UL).shift(LEFT)
        self.play(tr_time1.set_value, t2, run_time=7, rate_func=linear)
        self.wait()


import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim   --custom_folders  --disable_caching  -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)