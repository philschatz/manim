from manim import *



def lissajous_curve_func(t):
    return np.array((np.sin(3 * t), np.sin(4 * t)+2/3*PI, 0))


version_num = "0.1.1"


class TwitterScene(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        version = Tex(f"v{version_num}").to_corner(UR).set_color(BLACK)
        self.add(version)

        dot = Dot()


        dummy_func = ParametricFunction(lissajous_curve_func, t_max=TAU, fill_opacity=0)
        dummy_func.scale(2).move_to(ORIGIN)
        func1= dummy_func.copy().set_stroke(width=18)
        func1 = CurvesAsSubmobjects(func1)
        func1.set_color_by_gradient(YELLOW_A,YELLOW_D)
        func2= dummy_func.copy().set_color(BLACK).set_stroke(width=20)
        dot.add_updater(lambda m: m.move_to(dummy_func.get_end()))
        dummy_func.set_opacity(0)
        # or dummy_func.fade(1) )
        self.add(dot)
        self.play(
            ShowCreation(dummy_func),
            ShowCreation(func2),
            ShowCreation(func1),
            run_time=1
        )
        self.add(func1)
        self.wait()
        ## add twitter scene content here
        banner = ManimBanner(dark_theme=False).scale(0.3).to_corner(DR)
        self.play(FadeIn(banner))
        self.play(banner.expand())

import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim   --custom_folders  --disable_caching  -p --config_file '{project_path}/manim_settings.cfg' " + script_name)

