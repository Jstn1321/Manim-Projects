from manim import *
import math
#manim -pqh derivativeDef.py DerivativeDef
class DerivativeDef(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-1, 2.5], 
            y_range=[-1, 1],
            axis_config={"color": WHITE}
        )
        axes.add_coordinates()
        
        sin_graph = axes.plot(
            lambda x: np.sin(x),  
            stroke_color=BLUE     
        )

        self.play(Write(axes), run_time = 2)
        self.play(Create(sin_graph, run_time=2))
        self.wait()

        dota = Dot(color = RED)
        dota.move_to(axes.i2gp(0.3, sin_graph))
        self.play(FadeIn(dota,scale=0.5))

        dotb = Dot(color = RED)
        dotb.move_to(axes.i2gp(2, sin_graph))
        self.play(FadeIn(dotb,scale=0.5))

        dotb_tracker = ValueTracker(2)
        f_always(
            dotb.move_to,
            lambda: axes.i2gp(dotb_tracker.get_value(), sin_graph)
        )

       
        derv = always_redraw(
            lambda: axes.get_secant_slope_group(
                graph = sin_graph, 
                x = dota.get_center(), 
                dx = dotb_tracker.get_value() - 0.229, 
                secant_line_color = PURPLE, 
                secant_line_length = 6
                )
            )
        
        self.add(derv, run_time = 2)
        self.wait()
        self.play(dotb_tracker.animate.set_value(0.3), run_time = 5)
        self.wait()