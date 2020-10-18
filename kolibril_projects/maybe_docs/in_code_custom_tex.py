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