from manim import *
import matplotlib.pyplot as plt




class ConnectingMatplotlib(Scene):
    def construct(self):
        pyFrame = config["pixel_height"]  # 1080 default
        pxFrame = config["pixel_width"]  # 1920 #default
        frame_width = config["frame_width"]
        frame_height = config["frame_height"]
        d1 = Line(frame_width * LEFT / 2, frame_width * RIGHT / 2).to_edge(DOWN)
        self.add(d1)
        self.add(Tex(str(pxFrame)).scale(0.5).next_to(d1, DOWN, buff=0))
        d2 = Line(frame_height * UP / 2, frame_height * DOWN / 2).to_edge(LEFT)
        self.add(d2)
        self.add(Tex(str(pyFrame)).scale(0.5).rotate(90*DEGREES).next_to(d2, LEFT, buff=0))
        x_values = np.linspace(0, 30, 400)
        dpi_tracker = ValueTracker(100)
        dot = Dot()
        self.add(dot)
        self.add(Dot())
        dpi = 100
        # figsize = (4,4)
        for fig_val in np.arange(4,8, 0.1):
            fig_val = float(f"{fig_val:.2f}")
            x = np.linspace(0,10,100)
            print(dpi)
            figsize= (fig_val,fig_val)
            fig, ax = plt.subplots(figsize=figsize, dpi = dpi)
            ax.plot(x, np.sin(x))
            ax.set_ylim(-1,1)
            fig.canvas.draw()
            img = ImageMobject(fig.canvas.buffer_rgba())
            plt.close(fig)
            an1=Text(f"{figsize=}\n"
                     f"{dpi=}").to_edge(UP).scale(0.4)
            imgAll = Group(an1,img.next_to(an1,DOWN))
            self.add(imgAll)
            self.wait(1/config.frame_rate*2)
            self.remove(imgAll)
import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim   --custom_folders -i --disable_caching -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)
