from manim import *
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
MAX_N=400
X, y = make_blobs(
    n_samples=MAX_N,
    n_features=2,
    centers=3,
    cluster_std=0.8,
    shuffle=True,
    random_state=0,
)
def plot(param):
    fig, ax = plt.subplots(figsize = (4,3) , dpi = 250)
    param = int(param)
    X_show = X[:param, :]
    ax.set_xlim(-4,4)
    ax.set_ylim(-1,6)

    ax.scatter(X_show[:, 0], X_show[:, 1], s=50, c="lightgray", edgecolor="black")
    fig.canvas.draw()
    img = ImageMobject(fig.canvas.buffer_rgba())
    plt.close(fig)
    return img


class ShowScreenResolution(Scene):
    def construct(self):
        pyFrame = config["pixel_height"]  # 1080 default
        pxFrame = config["pixel_width"]  # 1920 #default
        frame_width = config["frame_width"]
        frame_height = config["frame_height"]
        d1 = Line(frame_width * LEFT / 2, frame_width * RIGHT / 2).to_edge(DOWN)
        self.add(d1)
        self.add(Tex(str(pxFrame)).scale(0.5).next_to(d1, DOWN, buff=0))
        d2 = Line(frame_height * UP / 2, frame_height * DOWN / 2).to_edge(LEFT)
        self.add(d2)
        self.add(
            Tex(str(pyFrame)).scale(0.5).rotate(90 * DEGREES).next_to(d2, LEFT, buff=0)
        )
        img = plot(0)
        self.add(Text("My animated plot").next_to(img,UP))
        self.play(FadeIn(img))
        tr_amplitude = ValueTracker(0)
        def update_image(mob):
            new_mob = plot(tr_amplitude.get_value())
            mob.become(new_mob)

        img.add_updater(update_image)
        self.play(tr_amplitude.set_value, MAX_N, run_time=3)


import os
import sys
from pathlib import Path

if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(
        f"manim   --custom_folders  --disable_caching  -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' "
        + script_name
    )
