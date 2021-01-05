from manim import *

from matplotlib import pyplot as plt
import numpy as np
from skimage import data
import cv2
from skimage.transform import resize
import matplotlib.pyplot as plt
from skimage.transform import resize
from skimage import io
import numpy as np
import cv2
from skimage.transform import resize
from skimage import io
import numpy as np
import cv2
def make_2_5D_image(image):

    def imstretch(a):
        m = a.min()
        M = a.max()
        return np.uint8((256-1)/(M-m) * (a-m))
    image=imstretch(image)

    img_to_shear = cv2.cvtColor(image, cv2.COLOR_RGB2RGBA)

    shear_factor= 2
    x_scale_factor=3

    pad= np.full((int(img_to_shear.shape[0]/shear_factor)+20, img_to_shear.shape[1]) ,0)
    new_pad = cv2.cvtColor(np.uint8(pad), cv2.COLOR_GRAY2BGRA)
    new_pad[:,:,3]=0 # setting alpha channel to zero
    camera_new=np.concatenate((img_to_shear ,new_pad) ,axis=0)

    camerax = []
    for i,row in enumerate(np.rot90(camera_new,1)):
        camerax.append(np.roll(row,int(i/shear_factor),axis=0))
    camerax=np.uint8(np.rot90(camerax,-1))

    cameraxx = resize(camerax, (camerax.shape[0], camerax.shape[1] // x_scale_factor),
                      anti_aliasing=True)

    cameraxx=imstretch(cameraxx)
    return cameraxx


from manim import *

class Images(Scene):
    def construct(self):

        import matplotlib.pyplot as plt
        from skimage import io
        im = io.imread('fiji_cropped.tif')
        new_imgs = im[::40,:,:]
        for i, img in enumerate(new_imgs):
            img= make_2_5D_image(img)
            img= ImageMobject(img).shift(6*LEFT+i*RIGHT).scale(0.6)
            self.add(img)
import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim -r 270,1024  --custom_folders  --disable_caching -s -p -c '#ece6e2' --config_file '{project_path}/manim_settings.cfg' " + script_name)