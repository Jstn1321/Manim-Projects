from manim import *
import numpy as np

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

        self.play(Write(axes), run_time=2)
        self.play(Create(sin_graph), run_time=2)
        self.wait()

        # Initial x positions for dots
        x_a = 0.3
        x_b = 2.0
        
        dota = Dot(color=RED).move_to(axes.i2gp(x_a, sin_graph))
        dotb = Dot(color=RED).move_to(axes.i2gp(x_b, sin_graph))
        self.play(FadeIn(dota, scale=0.5), FadeIn(dotb, scale=0.5))

        # Create secant line group using x-coordinates, not positions
        secant_group = axes.get_secant_slope_group(
            graph=sin_graph,
            x=x_a,
            dx=x_b - x_a,  # Difference in x-coordinates
            secant_line_color=PURPLE,
            secant_line_length=6
        )
        self.play(FadeIn(secant_group), run_time=2)
        self.wait()

        # Animate dotb moving
        dotb_tracker = ValueTracker(x_b)
        dotb.add_updater(lambda m: m.move_to(
            axes.i2gp(dotb_tracker.get_value(), sin_graph)
        ))
        
        # Update secant line during animation
        def update_secant(group):
            new_group = axes.get_secant_slope_group(
                graph=sin_graph,
                x=x_a,
                dx=dotb_tracker.get_value() - x_a,
                secant_line_color=PURPLE,
                secant_line_length=6
            )
            group.become(new_group)
        
        secant_group.add_updater(update_secant)
        
        self.play(dotb_tracker.animate.set_value(0.3), run_time=5)
        self.wait()