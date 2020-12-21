from manim import *

class KineticsPartA(Scene):
    def construct(self):

        GREY_BLACK = "#a9a9a9"
        SILVER = "#C0C0C0"
        silver_coord= [0,-2,0]
        silver_size= 0.15
        split_width=.1
        slit_annot= VGroup(Square(fill_opacity=0.3).set_color(BLACK), Square(0.4, fill_color=WHITE, fill_opacity=1, stroke_color=BLACK))
        slit_annot.apply_matrix(np.array([[0.5, 0.3,  0. ],
                                          [0 , 1.,  0. ],
                                          [0.,  0.,  1. ]]))
        slit_annot.rotate(angle=80*DEGREES,axis=LEFT)
        slit_annotA= slit_annot.copy()
        slit_annotA.move_to(silver_coord).shift(1.5*UP+2.5*LEFT)
        slit_annotA.title = Tex("Spalt A", color=BLACK).scale(0.5).next_to(slit_annotA,UP, buff=0.3*SMALL_BUFF)
        slit_annotB= slit_annot.copy()
        slit_annotB.move_to(silver_coord).shift(2.5*UP+2.5*LEFT)
        slit_annotB.title = Tex("Spalt B", color=BLACK).scale(0.5).next_to(slit_annotB,UP, buff=0.3*SMALL_BUFF)



        sq = Rectangle(height=6, width=2).set_color(BLACK)

        silv = Square(silver_size*2, fill_color=SILVER, stroke_color=SILVER, fill_opacity=1).move_to(silver_coord)
        silv.title = Tex("Silberquelle", color=BLACK).scale(0.5).next_to(silv,LEFT, buff=1.6)
        silv.title.shift(0.55*RIGHT)


        self.add(silv,silv.title)
        silver_holder = VGroup(Line([-1,-2,0],[0-silver_size,-2,0],color=BLACK),
                               Line([0+silver_size,-2,0],[1,-2,0], color=BLACK))
        self.add(sq)
        self.add(silver_holder)


        ### shooters:
        shootingdots = [Dot(silv.get_center()).set_color(BLACK) for _ in range(0,30)]

        for val, mobj in enumerate(shootingdots):
            mobj.move_to(silv.get_center()+1.3*UP)
            mobj.rotate(np.random.uniform( -np.radians(50), np.radians(50)  ) ,about_point= silv.get_center())
            mobj.set_opacity(0)
            mobj.subdot= Dot(point=silv.get_center(), fill_color=interpolate_color(SILVER, BLACK,0.8))
            mobj.time=val*1/len(shootingdots)

        def updater(mobj,dt):
            if mobj.time > 1:
                mobj.time=0
                mobj.move_to(silv.get_center() + 1.3*UP)
                mobj.rotate(np.random.uniform(-np.radians(50), np.radians(50)), about_point= silv.get_center())
            point= mobj.get_center() + (silv.get_center() - mobj.get_center()) * mobj.time
            point = silv.get_center() + (mobj.get_center() - silv.get_center())*mobj.time
            mobj.subdot.move_to(point)
            mobj.subdot.set_opacity(1-mobj.time)
            mobj.time += 1 / config["frame_rate"]*0.3

        self.add(silv)
        for mobj in shootingdots:
            mobj.subdot.scale(0.4)
            mobj.add_updater(updater)
            self.add(mobj,mobj.subdot)


        shootingdotslong = [Dot(silv.get_center()).set_color(BLACK) for _ in range(0,50)]
        distance2= 4
        for val, mobj in enumerate(shootingdotslong):
            mobj.move_to(silv.get_center()+4*UP)
            mobj.rotate(np.random.uniform( -np.radians(10), np.radians(10)  ) ,about_point= silv.get_center())
            mobj.set_opacity(0)
            mobj.subdot= Dot(point=silv.get_center(), fill_color=interpolate_color(SILVER, BLACK,0.8))
            mobj.val = np.random.poisson(30)
            mobj.time=val*1/len(shootingdotslong)

        def updaterlong(mobj,dt):
            if mobj.time > 1:
                mobj.time=0
                mobj.move_to(silv.get_center() + 4*UP)
                mobj.rotate(np.random.uniform(-np.radians(10), np.radians(10)), about_point= silv.get_center())
            point= mobj.get_center() + (silv.get_center() - mobj.get_center()) * mobj.time
            point = silv.get_center() + (mobj.get_center() - silv.get_center())*mobj.time
            mobj.subdot.move_to(point)
            mobj.subdot.set_opacity(1-mobj.time)
            mobj.time += 1 / config["frame_rate"]*0.01*mobj.val /distance2

            # self.add(silv)
        for mobj in shootingdotslong:
            mobj.subdot.scale(0.4)
            mobj.add_updater(updaterlong)
            self.add(mobj,mobj.subdot)
        self.bring_to_front(silv)
        self.wait(4)
        ### include the slits
        self.play(FadeIn(VGroup(slit_annotA,slit_annotA.title, slit_annotB,slit_annotB.title)))
        self.wait(2)
        slitA = VGroup(Line([-1,-0.5,0],[0-split_width,-0.5,0]),Line([0+split_width,-0.5,0],[1,-0.5,0])).set_color(BLACK)
        slitB = VGroup(Line([-1, 0.5,0],[0-split_width, 0.5,0]),Line([0+split_width, 0.5,0],[1, 0.5,0])).set_color(BLACK)
        self.play(slit_annotA.rotate, 9*DEGREES, LEFT, slit_annotB.rotate, 9*DEGREES, LEFT)
        self.play(FadeOutAndShift(slit_annotA, RIGHT), FadeOutAndShift(slit_annotB, RIGHT),FadeIn(slitA), FadeIn(slitB))
        slit_annotA.title.shift(RIGHT+0.3*DOWN)
        slit_annotB.title.shift(RIGHT+0.3*DOWN)

        ### shooters:
        shootingdotslong3 = [Dot(silv.get_center()).set_color(BLACK) for _ in range(0,50)]
        distance3= 4
        for val, mobj in enumerate(shootingdotslong3):
            mobj.move_to(silv.get_center()+4*UP)
            mobj.rotate(np.random.uniform( -np.radians(2), np.radians(2)  ) ,about_point= silv.get_center())
            mobj.set_opacity(0)
            mobj.subdot= Dot(point=silv.get_center(), fill_color=interpolate_color(SILVER, BLACK,0.8))
            mobj.val = np.random.poisson(30)
            mobj.time= val*1/len(shootingdotslong)

        def updaterlong3(mobj,dt):
            if mobj.time > 1:
                mobj.time=0
                mobj.move_to(silv.get_center() + 4*UP)
                mobj.rotate(np.random.uniform(-np.radians(1.4), np.radians(1.4)), about_point= silv.get_center())
            point= mobj.get_center() + (silv.get_center() - mobj.get_center()) * mobj.time
            point = silv.get_center() + (mobj.get_center() - silv.get_center())*mobj.time
            mobj.subdot.move_to(point)
            mobj.subdot.set_opacity(1-mobj.time)
            mobj.time += 1 / config["frame_rate"]*0.01*mobj.val /distance3

        for mobj in shootingdotslong:
            mobj.subdot.scale(0.4)
            mobj.remove_updater(updaterlong)
            self.remove(mobj,mobj.subdot)
        # self.add(silv)
        for mobj in shootingdotslong3:
            mobj.subdot.scale(0.4)
            mobj.add_updater(updaterlong3)
            self.add(mobj,mobj.subdot)
        self.bring_to_front(silv)
        self.wait(9)







import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim  --custom_folders  --disable_caching  -p  -c 'WHITE' --config_file '{project_path}/manim_settings.cfg' " + script_name)