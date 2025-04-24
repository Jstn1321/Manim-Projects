from manim import *
import math
#manim -pqh derivativeDef.py DerivativeDef
class DerivativeDef(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-5, 5], 
            y_range=[-5, 5],
            axis_config={"color": WHITE}
        )
        axes.add_coordinates()
        
        cubic_func = axes.plot(
            lambda x: 0.1*x*x,  
            stroke_color=BLUE,
            x_range=[-5,5,0.001]     
        )

        dx = ValueTracker(3)
        x = ValueTracker(1)

        self.play(Write(axes), run_time = 2)
        self.play(Create(cubic_func, run_time=2))
        self.wait()

        dota = always_redraw(lambda: Dot(color = RED))
        dota.move_to(axes.i2gp(x, cubic_func))
        self.play(FadeIn(dota,scale=0.5))

        dotb = Dot(color = RED)
        dotb.move_to(axes.i2gp(2, cubic_func))
        self.play(FadeIn(dotb,scale=0.5))

        dotb_tracker = ValueTracker(4)
        f_always(
            dotb.move_to,
            lambda: axes.i2gp(dotb_tracker.get_value(), cubic_func)
        )

        

        derv = always_redraw(lambda : axes.get_secant_slope_group(graph = cubic_func, x = x.get_value(),dx = dx.get_value(), secant_line_color=PURPLE, dy_line_color= YELLOW, dx_line_color=GREEN, secant_line_length=9))

        self.play(Create(derv))
        self.play(dx.animate.set_value(0.01),dotb_tracker.animate.set_value(0.3), run_time = 8)
        self.wait()
        self.remove(dotb)
        self.play(x.animate.set_value(-2), run_time = 6)
        self.wait()
        self.play(x.animate.move_to(2), run_time = 8)
        self.wait()