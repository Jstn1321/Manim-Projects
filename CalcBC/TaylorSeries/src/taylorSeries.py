from manim import *

class TaylorSeries(Scene):
    def construct(self):
        axes = Axes(
            x_range = [-10, 10],
            y_range = [-10, 10],
            axis_config={"include_tip": False}
        ).to_edge(DOWN, buff=0.5)

        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

        title = Tex("The Taylor Series")
        

        self.play(Write(title))
        self.wait(1.5)
        self.play(title.animate.to_edge(UP, buff=1), Write(axes), Write(axes_labels))