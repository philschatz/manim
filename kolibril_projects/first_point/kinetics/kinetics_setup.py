from manim import *

class Kinetics(Scene):
    def construct(self):
        sq= Square(1).set_color(BLACK).set_fill(opacity=1  )
        shootingdots = [Dot(sq.get_center()).set_color(BLACK) for _ in range(0,30)]

        for val, mobj in enumerate(shootingdots):
            mobj.move_to(sq.get_center()+1.5*UP)
            mobj.rotate(np.random.uniform( -np.radians(30), np.radians(30)  ) ,about_point= sq.get_center())
            mobj.set_opacity(0)
            mobj.subdot= Dot(point=sq.get_center()).set_color(RED)
            mobj.time=val*1/len(shootingdots)

        def updater(mobj,dt):
            if mobj.time > 1:
                mobj.time=0
                mobj.move_to(sq.get_center() + 1.5*UP)
                mobj.rotate(np.random.uniform(-np.radians(30), np.radians(30)), about_point= sq.get_center())
            point= mobj.get_center() + (sq.get_center() - mobj.get_center()) * mobj.time
            point = sq.get_center() + (mobj.get_center() - sq.get_center())*mobj.time
            mobj.subdot.move_to(point)
            mobj.subdot.set_opacity(1-mobj.time)
            mobj.time += 1 / config["frame_rate"]*0.3

        self.add(sq)
        for mobj in shootingdots:
            mobj.subdot.scale(1.4)
            mobj.add_updater(updater)
            self.add(mobj,mobj.subdot)
        self.bring_to_front(sq)
        self.wait(4)
import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim  -m --custom_folders  --disable_caching  -p -c 'WHITE' --config_file '{project_path}/manim_settings.cfg' " + script_name)