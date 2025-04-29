from manim import *
import math

class mvt(Scene):
    def construct(self):

        axes = Axes(
            x_range = [0, 3],
            y_range = [0, 7],
            axis_config = {"include_tip" : False}
        ).to_edge(DL, buff=0.5).add_coordinates()

        axes_label = axes.get_axis_labels(x_label="x", y_label="y")

        func = axes.plot(
            lambda x: -(x)**3 + 3*x**2+x,
            stroke_color = BLUE
        )

        mvtAb = Text(r"The MVT")
        mvtExp = Text(r"The Mean Value Theorum")
        mvtDef = Text("for a continuous and differentiable function, there exists \n a point where the derivative equals the average \n rate of change over an interval").scale(0.8)
        mvtAbP2 = Text(r"The MVT").shift(UP*1.5)

        self.play(Write(mvtAb))
        self.wait(1.5)
        self.play(ReplacementTransform(mvtAb, mvtExp))
        self.wait(1.5)
        self.play(mvtExp.animate.shift(UP*1.5), Write(mvtDef))
        self.wait(6)
        self.play(ReplacementTransform(mvtExp, mvtAbP2), FadeOut(mvtDef))
        self.play(mvtAbP2.animate.to_edge(UP, buff=1), Write(axes), Write(axes_label), Write(func))
        self.wait(1.5)