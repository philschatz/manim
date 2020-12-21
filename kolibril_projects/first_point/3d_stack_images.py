from manim import *

from matplotlib import pyplot as plt
import numpy as np
from skimage import data
import cv2
from skimage.transform import resize

def make_2_5D_image():
    camera = data.camera()
    camera = cv2.cvtColor(camera, cv2.COLOR_RGB2RGBA)

    shear_factor= 2
    x_scale_factor=3

    pad= np.full((int(camera.shape[0]/shear_factor), camera.shape[1]) ,0)
    new_pad = cv2.cvtColor(np.uint8(pad), cv2.COLOR_GRAY2BGRA)
    new_pad[:,:,3]=0 # setting alpha channel to zero
    camera_new=np.concatenate((camera ,new_pad) ,axis=0)

    camerax = []
    for i,row in enumerate(np.rot90(camera_new,1)):
        camerax.append(np.roll(row,int(i/shear_factor),axis=0))
    camerax=np.uint8(np.rot90(camerax,-1))

    cameraxx = resize(camerax, (camerax.shape[0], camerax.shape[1] // x_scale_factor),
                      anti_aliasing=True)
    def imstretch(a):
        m = a.min()
        M = a.max()
        return np.uint8((256-1)/(M-m) * (a-m))
    cameraxx=imstretch(cameraxx)
    return cameraxx

from manim import *

class Images(Scene):
    def construct(self):
        img= make_2_5D_image()
        imgs = [ImageMobject(img).shift(4*LEFT+i*RIGHT) for i in range(0,10)]
        self.add(Line(imgs[0].get_bottom(), imgs[-1].get_bottom() , stroke_width=10, stroke_color=BLACK)\
            .shift(UP*(imgs[0].get_top()-imgs[0].get_bottom())/6))
        for img in imgs:
            self.play(FadeInFrom(img, UP) , run_time=0.4)

        self.wait(1)

import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim   --custom_folders  --disable_caching  -p -c '#ece6e2' --config_file '{project_path}/manim_settings.cfg' " + script_name)