from manim import *

class Gauss(Scene):
    def construct(self):
        A = np.array([-2,-1,0])
        B = np.array([2,-1,0])
        C = np.array([0,2,0])
        triang = Polygon(A,B,C)
        lineA1= Line(A,B , color=YELLOW)
        lineB1= Line(B,C , color=YELLOW)
        B_ext= B + (B-A)/np.linalg.norm(B-A)
        lineA2= DashedLine(B ,B_ext , color=YELLOW)
        self.add(triang)
        lineA=VGroup(lineA1,lineA2)
        self.play(ShowCreation(lineA), run_time=2)
        pairs = [
            (lineA1.get_angle(), lineB1.get_angle())]
        arcs = []
        for start, angle in pairs:
            arc = Arc(
                angle = angle,
                radius = 1,
                start_angle = start,
                color = GREEN
            )
            arcs.append(arc)
        arc[0].shift(B)
        alpha = MathTex("\\alpha").scale(0.6)
        beta = MathTex("\pi-\\alpha").scale(0.6)
        alpha.next_to(B, 1*UP+1.5*LEFT)
        beta.next_to(B, 1*UP+0.2*RIGHT)
        angleB= VGroup(arc[0],alpha,beta)
        self.play(ShowCreation(angleB))

import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders  --disable_caching -s -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)