
from manim import *

class Text(Scene):
    CONFIG = {
        "y_min": 0,
        "y_max": 10    }
    def construct(self):
        sq= Square()
        self.add(sq)
        self.play(sq.set_color, GREEN)
        self.wait()

from pathlib import Path
if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders  -s -p -c 'BLACK' --config_file '/home/jan-hendrik/.config/JetBrains/PyCharm2020.2/scratches/my_config.cfg' " + script )
