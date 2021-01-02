from manim import *


# note: only working when there are the corresponding images in the img_sk folder !

def Folderscanner(interval):
    import glob
    filenames = [img for img in glob.glob(f"img_sk/{interval}*")]
    filenames.sort()
    return filenames


class VideoSceneFinal1(Scene):

    def construct(self):
        def get_image(imgs_list, image_number):
            return ImageMobject(imgs_list[int(image_number)]).scale(3.4).to_edge(UP)

        imgsA = Folderscanner("A")
        imgsB = Folderscanner("B")
        imgsC = Folderscanner("C")
        imgsD = Folderscanner("D")
        print(imgsA)
        dot = get_image(imgsA, 0)
        self.add(dot)

        def Tiny_Updater(dots, val_trackerX):
            def small_change2(mob):
                val = int(val_trackerX.get_value())
                print(val)
                mob.become(get_image(imgs, val))
                return mob

            return UpdateFromFunc(dots, small_change2)

        tick_start = 0
        tick_end = len(imgsA)
        val_tracker = ValueTracker(tick_start)
        imgs = imgsA
        t1 = TextMobject("1. Measuring").set_color(BLACK).scale(0.5).next_to(dot, direction=DOWN, aligned_edge=RIGHT,
                                                                             buff=0.1)
        self.add(t1)
        self.wait()

        self.play(Tiny_Updater(dot, val_tracker), val_tracker.set_value, tick_end, rate_func=smooth, run_time=2.5)
        self.wait()
        dot2 = get_image(imgsB, 0)
        t2 = TextMobject("2. Clustering").set_color(BLACK).scale(0.5).next_to(dot, direction=DOWN, aligned_edge=RIGHT,
                                                                              buff=0.1)
        t1.become(t2)
        self.play(FadeIn(dot2))
        dot3 = get_image(imgsB, 1)
        self.play(FadeIn(dot3))
        self.remove(dot)
        self.remove(dot2)
        tick_start = 1;
        tick_end = len(imgsB)
        imgs = imgsB
        val_tracker = ValueTracker(tick_start)
        self.play(Tiny_Updater(dot2, val_tracker), val_tracker.set_value, tick_end, rate_func=linear, run_time=10)
        self.wait(1)


import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders  --disable_caching -s -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)