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

        self.play(Write(axes))
        self.play(Create(sin_graph, run_time=2))
        self.wait()

        