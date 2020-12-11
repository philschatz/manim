from manim import *
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 150


class GraphExample(Scene):
    def construct(self):
        def f(x):
            return x**2
        fig, ax = plt.subplots()
        x= np.arange(0,100,1)
        ax.plot(x, f(x))
        fig.canvas.draw()
        img = ImageMobject(fig.canvas.buffer_rgba()).scale(0.8).to_edge(RIGHT)
        plt.close(fig)
        self.add(img)
        code=Code("/home/jan-hendrik/projects/manim-community/kolibril_projects/first_point/code_matplotlib_tex_idea/mycode.py",tab_width=6).next_to(img, LEFT)
        form=MathTex("f(x)= x^2").next_to(code,UP).align_to(code,LEFT)
        self.add(code,form)
        def f2(x):
            return np.sin(x)
        fig, ax = plt.subplots()
        x= np.arange(0,20,0.1)
        ax.plot(x, f2(x))
        fig.canvas.draw()
        img2 = ImageMobject(fig.canvas.buffer_rgba()).scale(0.8).to_edge(RIGHT)
        plt.close(fig)
        code2=Code("/home/jan-hendrik/projects/manim-community/kolibril_projects/first_point/code_matplotlib_tex_idea/mycode2.py",tab_width=6).next_to(img, LEFT)
        form2=MathTex("f(x)= \sin(x)").next_to(code,UP).align_to(code,LEFT)
        self.wait()
        self.play(Transform(form,form2), FadeIn(code2), FadeIn(img2), run_time=3)
        self.wait()


import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim   --custom_folders  --disable_caching -s -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)