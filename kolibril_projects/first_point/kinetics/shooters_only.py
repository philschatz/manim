from manim import *

class SSS(Scene):
    def construct(self):

        GREY_BLACK = "#a9a9a9"
        SILVER = "#C0C0C0"
        silv= Square().shift(2*DOWN).scale(0.2).set_color(BLACK)
        ### shooters:
        shootingdots = [Dot(silv.get_center()).set_color(BLACK) for _ in range(0,30)]
        distance1 = 1.3
        for val, mobj in enumerate(shootingdots):
            mobj.move_to(silv.get_center()+distance1*UP)
            mobj.rotate(np.random.uniform( -np.radians(50), np.radians(50)  ) ,about_point= silv.get_center())
            mobj.set_opacity(0)
            mobj.subdot= Dot(point=silv.get_center(), fill_color=interpolate_color(SILVER, BLACK,0.8))
            mobj.val = np.random.poisson(30)
            mobj.time=val*1/len(shootingdots)

        def updater(mobj,dt):
            if mobj.time > 1:
                mobj.time=0
                mobj.move_to(silv.get_center() + distance1*UP)
                mobj.rotate(np.random.uniform(-np.radians(50), np.radians(50)), about_point= silv.get_center())
            point= mobj.get_center() + (silv.get_center() - mobj.get_center()) * mobj.time
            point = silv.get_center() + (mobj.get_center() - silv.get_center())*mobj.time
            mobj.subdot.move_to(point)
            mobj.subdot.set_opacity(1-mobj.time)
            mobj.time += 1 / config["frame_rate"]*0.01*mobj.val

        # self.add(silv)
        for mobj in shootingdots:
            mobj.subdot.scale(0.4)
            mobj.add_updater(updater)
            self.add(mobj,mobj.subdot)
        self.bring_to_front(silv)
        self.wait(4)

import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim -m  --custom_folders  --disable_caching  -p  -c 'WHITE' --config_file '{project_path}/manim_settings.cfg' " + script_name)