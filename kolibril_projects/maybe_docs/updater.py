from manim import *



def control_anim_with_alpha(anim,alpha):
    anim.begin()
    anim.interpolate(alpha)

class AnimFunc  (Scene):
    def construct(self):
        triangle = Triangle().set_height(4)
        triangle.save_state()

        def update(mob,alpha):
            mob.restore()
            control_anim_with_alpha(FadeToColor(mob,RED),alpha)
            control_anim_with_alpha(ApplyMethod(mob.scale,0.5),alpha)
            control_anim_with_alpha(ApplyMethod(mob.rotate,PI/2),alpha)

        self.add(triangle)
        self.play(
            UpdateFromAlphaFunc(triangle,update),
            run_time=4
        )
        self.wait()

import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders  --disable_caching  -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)