from manim import *
import math
#manim -pqh derivativeDef.py DerivativeDef
class DerivativeDef(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-5, 5], 
            y_range=[-1, 4],
            y_length=5,
            axis_config={"color": WHITE, "include_tip": False, "include_numbers": True},
        ).to_edge(DOWN)
        axes.add_coordinates()
        
        func = axes.plot(
            lambda y: 0.1 * y * y,  
            stroke_color=BLUE,
            x_range=[-5,5,0.001]     
        )

        top = Tex("The Derivative")        

        self.play(Write(top), runtime = 4)
        self.wait(1.5)
        self.play(top.animate.to_edge(UP, buff=1))
        self.play(Write(axes), run_time = 2)
        self.play(Create(func, run_time=2))
        self.wait()

        

        dota = Dot(color = RED)
        dota.move_to(axes.i2gp(1, func))
        self.play(FadeIn(dota,scale=0.5))

        dotb = Dot(color = RED)
        dotb.move_to(axes.i2gp(4, func))
        self.play(FadeIn(dotb,scale=0.5))

        dotb_tracker = ValueTracker(4)
        f_always(
            dotb.move_to,
            lambda: axes.i2gp(dotb_tracker.get_value(), func)
        )

        
        dx = ValueTracker(3)
        x = ValueTracker(1)
        derv = always_redraw(lambda : axes.get_secant_slope_group(graph = func, x = x.get_value(),dx = dx.get_value(), secant_line_color=PURPLE, dy_line_color= YELLOW, dx_line_color=GREEN, secant_line_length=8))

        f_always(
            dota.move_to,
            lambda: axes.i2gp(x.get_value(), func)
        )
        

        self.play(Create(derv))
        self.play(dx.animate.set_value(0.01),dotb_tracker.animate.set_value(1), run_time = 8)
        self.wait()
        self.remove(dotb)
        self.play(x.animate.set_value(-3), run_time = 4)
        self.wait()
        self.play(x.animate.move_to(3), run_time = 4)
        self.wait()