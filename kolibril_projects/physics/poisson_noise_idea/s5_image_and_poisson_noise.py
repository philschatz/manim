from kolibril_projects.physics.poisson_noise_idea.histo_3b1b import Image_Histogram
from manim import *

def circ(img, radius, circle_opacity):
    n, m = np.shape(img)
    for j in range(0, n):
        for k in range(0, m):
            if (j - n / 2) ** 2 + (k - m / 2) ** 2 < radius ** 2:
                img[j, k] = img[j, k] * (1 - circle_opacity)
    return img


def create_poission_noise_ball(num_photons=100):
    num_pixels = 512
    img_origin = np.ones((num_pixels, num_pixels))
    shot_noise_img = num_photons * img_origin
    shot_noise_img = circ(shot_noise_img, 75, circle_opacity=0.1)
    shot_noise = np.random.poisson(shot_noise_img, (num_pixels, num_pixels))
    return shot_noise

# def add_circle

def create_image(num_photons=100):
    num_pixels = 512
    img_origin = np.ones((num_pixels, num_pixels))
    image = num_photons * img_origin
    return np.uint8(image)


def IPcontraststretch(image):
    image = np.asarray(image)
    M = image.max()
    m = image.min()
    if m == M:
        return np.uint8(image*0+255)
    stretched_img = (256 - 1) / (M - m) * (image - m)
    return np.uint8(stretched_img)

class Poisson_noise(Scene):
    def construct(self):
        seed = 42 # initilize the randomness for the poisson noise
        np.random.RandomState(seed)
        poission_With_one_pixel=[]
        text_for_the_images= []
        histograms= []
        rep_rate=1
        photon_intensities= range(1,20)
        rep_rate=1
        # photon_intensities=[1]
        #
        max = 256


        for photons_val in photon_intensities:
            for i in range(0,rep_rate):
                 img=create_poission_noise_ball(num_photons=photons_val)
                 img[img > max-1]=max-1
                 im_sctretched=IPcontraststretch(img)
                 poission_With_one_pixel.append(im_sctretched)
                 text_for_the_images.append(str(photons_val))

                 val = np.histogram(img, bins=[i for i in np.arange(0, max + 1)])
                 hist = Image_Histogram(val[1], val[0], x_scale=4 / max, y_scale=3/val[0].max())
                 histograms.append(hist)
                 print(photons_val)

        poission_With_one_pixel_ALL= [ImageMobject(img_a).scale(2.5) for img_a in poission_With_one_pixel]

        for PLOT,text,hist in zip(poission_With_one_pixel_ALL,text_for_the_images,histograms):
            self.clear()
            PLOT.to_edge(LEFT)
            self.add(PLOT)
            print(text)
            t_2= MathTex(r"\text{Photonenrate: }" + text +  r"\, \frac{\text{photons}}{s}")
            t_2.next_to(PLOT,DOWN)
            t_2.to_edge(LEFT)
            self.add(t_2)
            hist.to_edge(RIGHT)
            self.add(hist)
            print(text)
            self.wait(0.33)



import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders  --disable_caching -s -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)







