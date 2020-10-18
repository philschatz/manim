from manim import *
from sklearn.datasets import make_blobs

DRAC_ORANGE = "#CC7832"


class PCA(ThreeDScene):
    def construct(self):
        self.begin_ambient_camera_rotation(0.2)
        self.set_camera_orientation(phi=45 * DEGREES, theta=-45 * DEGREES)
        self.add(ThreeDAxes())
        centers = [[1, 1.2, 1.6], [0.9, 0.2, 2.9], [0.4, 0.5, 1.8]]
        # create dataset6
        X, y = make_blobs(
            n_samples=40, n_features=3,
            centers=centers, cluster_std=0.4,
            shuffle=False, random_state=0
        )
        A = X.T[0]
        B = X.T[1]
        C = X.T[2]

        Dots = VGroup(*[Dot(point=(a, b, c)) for a, b, c in zip(A, B, C)])
        Dots_shaddow = Dots.copy().set_opacity(0.1)
        Dots_z0 = Dots.copy().set_color(DRAC_ORANGE)
        rect = Rectangle(width=3, height=3, fill_color=DRAC_ORANGE, fill_opacity=0.2, stroke_color=WHITE).set_shade_in_3d(True)
        rect.shift(UP + RIGHT)
        self.add(rect)
        self.add(Dots)
        self.add(Dots_shaddow)
        [objec.set_z(0) for objec in Dots_z0.submobjects]
        self.wait()
        self.play(Transform(Dots, Dots_z0), run_time=1)
        self.wait()


import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim   --custom_folders  --disable_caching  -p  -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)