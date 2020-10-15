from manim import *
import matplotlib.pyplot as plt

# is this really right??

from manim import *
import matplotlib.pyplot as plt


def get_image_plot(t, dispersion):
    def n(wj):
        if dispersion == "high":
            return 1 + wj * 0.01
        if dispersion == "low":
            return 1.1 - wj * 0.01
        if dispersion == "const":
            return 1

    c = 1
    num_of_waves = 121
    start_w = 1
    end_w = 7
    x = np.linspace(-25, 100, 10001)

    def g(x, t):
        u1 = 0
        for wj in np.linspace(start_w, end_w, num_of_waves):
            u1 += np.exp(1j * (wj * n(wj) / c * x - t * wj))
        return u1.real

    fig, ax = plt.subplots(figsize=(14, 3))
    ax.set_xlim(-15, 100)
    ax.set_ylim(-80, 122)
    ax.annotate(r'x in [m]',
                xy=(1, 0), xycoords='axes fraction',
                xytext=(-20, 20), textcoords='offset pixels',
                horizontalalignment='right',
                verticalalignment='bottom',
                fontsize=20)
    ax.plot(x, g(x, t))
    fig.canvas.draw()
    img = ImageMobject(fig.canvas.buffer_rgba()).scale(1.3)
    plt.close("all")
    return img


class WConst(Scene):

    def construct(self):
        t1 = 1
        t2 = 90
        tr_time3 = ValueTracker(t1)

        tr_time1 = ValueTracker(t1)
        image1 = get_image_plot(tr_time1.get_value(), dispersion="const")

        def update_image1(mob):
            new_mob = get_image_plot(
                tr_time3.get_value(), dispersion="const"
            )
            new_mob.move_to(mob.get_center())
            mob.become(new_mob)

        image1.add_updater(update_image1)

        tr_time2 = ValueTracker(t1)

        image2 = get_image_plot(tr_time2.get_value(), dispersion="high")

        def update_image2(mob):
            new_mob = get_image_plot(
                tr_time3.get_value(), dispersion="high")
            new_mob.move_to(mob.get_center())
            mob.become(new_mob)

        image2.add_updater(update_image2)

        image3 = get_image_plot(tr_time3.get_value(), dispersion="low")

        def update_image3(mob):
            new_mob = get_image_plot(
                tr_time3.get_value(), dispersion="low")
            new_mob.move_to(mob.get_center())
            mob.become(new_mob)

        image3.add_updater(update_image3)

        self.add(image1, image2, image3)
        image1.next_to(image2, UP, buff=0)
        image3.next_to(image2, DOWN, buff=0)
        image1.shift(RIGHT)
        image2.shift(RIGHT)
        image3.shift(RIGHT)
        lab1 = MathTex(r"\frac{\partial n}{\partial \omega} =0").set_color(BLACK)
        lab2 = MathTex(r"\frac{\partial n}{\partial \omega} >0").set_color(BLACK)
        lab3 = MathTex(r"\frac{\partial n}{\partial \omega} <0").set_color(BLACK)
        lab1.next_to(image1,LEFT, buff=-0.3)
        lab2.next_to(image2,LEFT, buff=-0.3)
        lab3.next_to(image3,LEFT, buff=-0.3)
        self.add(lab1,lab2,lab3)
        self.play(tr_time3.set_value, t2, run_time=12, rate_func=linear)
        self.wait()


import os;
import sys
from pathlib import Path

if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(
        f"manim  --custom_folders  --disable_caching  -p -c 'WHITE' --config_file '{project_path}/manim_settings.cfg' " + script_name)

