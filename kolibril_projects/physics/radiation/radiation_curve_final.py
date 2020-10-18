from pathlib import Path

from manim import *

class Radiation(Scene):
    def construct(self):
        offset=3.5*LEFT
        img = Path.home()/"Documents" /"manim_resources"/ "earth.png"
        earth= ImageMobject(str(img))
        heading= Tex(r"Earth radiation spectrum").to_edge(UP).scale(2)
        self.add(heading)
        earth.shift(offset).scale(1.3)
        y_text= Tex("Heat radiation from earth")
        y_text.rotate(np.pi/2)
        x_text= Tex("wavelength")
        x_teo=np.loadtxt("teoX.csv")/100000*3
        y_teo=np.loadtxt("teoY.csv")/1000*3
        x_exp=np.loadtxt("messX.csv")/100000*3
        y_exp=np.loadtxt("messY.csv")/1000*3
        curve_teo = VMobject()
        point=Dot([x_exp[119], y_exp[119],0])
        co2ar=Arrow(point.get_center()+1.2*DOWN, point.get_center(), color=ORANGE)
        co2_text= MathTex(r"\text{Caused by CO}_2",color=ORANGE).next_to(co2ar,DOWN)
        curve_teo.set_points_smoothly([[xi,yi,0]
        for xi, yi in zip(x_teo,y_teo) ] )
        curve_exp = VMobject()
        curve_exp.set_points_smoothly([[xi,yi,0]
                                   for xi, yi in zip(x_exp,y_exp) ] )
        curve_teo.set_style(stroke_width=4)
        curve_teo2= curve_teo.copy().set_style(stroke_opacity=0.5)
        text_teo= Text("Theory without atmosphere").scale(0.8)
        text_exp= Text("Satellite measurement").scale(0.8)
        x_text.scale(0.4).next_to(curve_teo,DOWN)
        x_text.align_to(curve_teo,LEFT)
        text_teo.next_to(curve_teo,UP)
        text_teo.align_to(curve_teo,RIGHT)
        y_text.scale(0.4).next_to(curve_teo, LEFT)
        y_text.align_to(curve_teo,DOWN)
        text_exp.next_to(curve_teo,UP)
        text_exp.align_to(curve_teo,RIGHT)
        self.add(y_text,text_teo,x_text,curve_teo)
        self.add(curve_teo2)
        self.add(earth)

        N=400
        R= np.random.uniform(1.4,1.7, (N,1))
        PHI= np.random.uniform(1,2*np.pi+1, (N,1))
        co2s= np.array([[float(r*np.sin(phi)), float(r*np.cos(phi)) ,0] for r,phi in zip(R,PHI)])
        dots=VGroup(*[Dot(point=co2+offset, fill_opacity=0.4,radius=0.05) for co2 in co2s ])
        dots0=dots.copy().scale(0.6).set_style(fill_opacity=0)
        self.add(dots0)
        self.play(Transform(dots0,dots,lag_ratio=0.01), Transform(curve_teo,curve_exp), run_time=10)
        self.play(FadeOut(text_teo), FadeIn(co2ar), FadeIn(co2_text), FadeIn(text_exp))
        self.wait(3)


import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim   --custom_folders  --disable_caching  -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)