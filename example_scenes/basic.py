from manim import *

class InCodeTexTemplateExample(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{amsfonts}")
        myTemplate.tex_compiler = "pdflatex"
        myTemplate.output_format = ".pdf"
        text = MathTex(r"\mathbb{M} ", tex_template=myTemplate)
        self.play(Write(text))
        self.wait(1)

import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders  --disable_caching -s -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)