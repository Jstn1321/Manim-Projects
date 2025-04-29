from manim import *
import math

class mvt(Scene):
    def construct(self):

        axes = Axes(
            x_range = [0, 3],
            y_range = [0, 5],
            axis_config = {"include_tip" : False}
        ).to_edge(DL, buff=0.5).add_coordinates()

        axes_label = axes.get_axis_labels(x_label="x", y_label="y")

        func = axes.plot(
            lambda x: -(x-1)**3 + x**2,
            stroke_color = BLUE
        )

        mvtAb = Text(r"The MVT")
        mvtExp = Text(r"The Mean Value Theorum")
        mvtDef = Tex("for a continuous and differentiable function, there exists \n a point where the derivative equals the average \n rate of change over an interval")

        self.play(Write(mvtAb))
        self.wait(1.5)
        self.play(ReplacementTransform(mvtAb, mvtExp))
        self.wait(1.5)
        self.play(mvtExp.animate.shift(UP*1.5), Write(mvtDef))