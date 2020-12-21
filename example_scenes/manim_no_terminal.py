import matplotlib.pyplot as plt
from manim import *

class Example(Scene):
    def construct(self):
        circle = Circle()
        self.add(circle)
        self.wait()

scene = Example()
scene.render()
data = scene.renderer.get_frame()
plt.imshow(data)
