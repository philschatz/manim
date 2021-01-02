from manim import *

class ABC(MovingCameraScene):
    def construct(self):
        img1 = ImageMobject("olaf/olaf01.jpg")
        img2 = ImageMobject("olaf/olaf02.jpg")
        img3 = ImageMobject("olaf/olaf03.jpg")
        img4 = ImageMobject("olaf/olaf04.jpg")
        img5 = ImageMobject("olaf/olaf05.jpg")
        img6 = ImageMobject("olaf/olaf06.jpg")
        img7 = ImageMobject("olaf/olaf07.jpg")
        img8 = ImageMobject("olaf/olaf08.jpg")
        img9 = ImageMobject("olaf/olaf09.jpg")
        img10 = ImageMobject("olaf/olaf10.jpg")
        img11 = ImageMobject("olaf/olaf11.jpg")

        self.play(FadeInFromLarge(img1))
        self.play(FadeInFrom(img2, LEFT))
        img3.shift(DOWN+RIGHT*4)
        self.add(img3)
        self.play(self.camera_frame.move_to, img3.get_center() , self.camera_frame.scale, 1.3)
        self.remove(*self.mobjects)
        self.camera_frame.move_to(ORIGIN)
        self.camera_frame.scale(1/1.3)
        self.add(Square(10, fill_opacity=1))
        dots = [img4.copy().scale(0.2).move_to([x,y,0]) for x,y in zip(np.random.uniform(-3,3,30),np.random.uniform(-3,3,30))]
        self.play(FadeInFromLarge(Group(*dots), lag_ratio=1, run_time=3))
        self.play(FadeOutAndShift(Group(*dots), DOWN, lag_ratio=1, run_time=3))
        self.add(img5)
        all_sparcs= VGroup()
        for theta in np.random.uniform(0, TAU , 43):
            def func2(t):
                v0=10
                g= 9.81
                return np.array((v0*t*np.cos(theta), v0*t*np.sin(theta)-0.5*g*t**2, 0))
            sparcle = ParametricFunction(func2,t_min=0.04, t_max=0.3, fill_opacity=0).set_color(ORANGE)
            all_sparcs.add((sparcle.shift(UP*0.9+LEFT*0.1)))
        self.play(*[Write(x) for x in all_sparcs.submobjects], run_time= 0.8, rate_func= linear)
        self.remove(*all_sparcs.submobjects)
        self.play(img5.rotate,90*DEGREES, UP)
        self.remove(img5)
        self.play(FadeInFromPoint(img6.scale(2),ORIGIN))
        img6.add_updater(lambda x: x.rotate(0.4))
        img6.add_updater(lambda x: x.scale(0.9))

        self.play(FadeOut(img6))
import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim   --custom_folders  --disable_caching  -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)