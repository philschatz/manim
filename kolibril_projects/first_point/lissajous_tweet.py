from manim import *

text = r"""
\begin{filecontents}{\jobname.bib}
@book{key,
  author = {Author, A.},
  year = {2001},
  title = {Title},
  publisher = {Publisher},
}
\end{filecontents}

\begin{document}

Hello World^\cite{key}

\bibliographystyle{plain}
\bibliography{\jobname}

\end{document}
"""

class AddPackageLatex(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\documentclass{article}")
        tex = Tex(text, tex_template=myTemplate).scale(3)
        self.add(tex)

import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders  --disable_caching -s -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)