from manim import *


class AnimFunc1(Scene):
    def construct(self):
        dot = Dot(radius=3)
        anim = FadeToColor(dot, RED_D)
        anim.begin()
        anim.interpolate(0.5)
        self.add(dot)

def control_anim_with_alpha(anim,alpha):
    anim.begin()
    anim.interpolate(alpha)

class AnimFunc2(Scene):
    def construct(self):
        triangle = Triangle().set_height(4)
        triangle.save_state()

        def update(mob,alpha):
            mob.restore()
            control_anim_with_alpha(FadeToColor(mob,RED),alpha)
            control_anim_with_alpha(ApplyMethod(mob.scale,0.5),alpha)
            control_anim_with_alpha(ApplyMethod(mob.rotate,PI/2),alpha)

        self.add(triangle)
        self.play(
            UpdateFromAlphaFunc(triangle,update),
            run_time=4
        )
        self.wait()
