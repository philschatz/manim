from manim import *

class shape(ThreeDScene):

    def construct(self):
        resolution_fa=22
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)

        def param_plane(u,v):
            x=u
            y=v
            z=0
            return np.array([x,y,z])
        magic_plane=  ParametricSurface((param_plane) , resolution=(resolution_fa,resolution_fa),
                                        v_min = -2, v_max = 2, u_min = -2, u_max = 2).scale_about_point(2,ORIGIN)
        def param_gauss(u,v):
            x=u
            y=v
            d = np.sqrt(x * x + y * y)
            sigma, mu = 0.4, 0.0
            z= np.exp(-((d - mu) ** 2 / (2.0 * sigma ** 2)))
            return np.array([x,y,z])

        magic_gauss= ParametricSurface((param_gauss),resolution=(resolution_fa, resolution_fa),
                                       v_min=-2,v_max=2,u_min=-2,u_max=2).scale_about_point(2,ORIGIN)
        magic_gauss.set_style(fill_opacity=1)
        magic_gauss.set_style(stroke_color=GREEN)
        magic_gauss.set_fill_by_checkerboard(GREEN,BLUE,opacity=0.1)
        axes = ThreeDAxes()
        self.add(axes)
        self.play(Write(magic_plane))
        self.play(Transform(magic_plane,magic_gauss))
        self.wait(2)


import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders  --disable_caching -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)