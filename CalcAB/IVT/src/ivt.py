from manim import *

class ivt(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 3],
            y_range=[0, 4],
            axis_config = {"include_tip" : False}
        ).to_edge(DL, buff=0.5)

        graph1 = axes.plot(
            lambda x: x**2,
            stroke_color = BLUE
        )

        title = Tex("The IVT")
        titleTopLeft = Text("IVT")
        expTitle = Tex("The Intermediate Value Theorum")
        defIvt = Tex("If a continuous function changes from one value to another over an interval, it must take on every value in between").scale(0.8)

        self.play(Write(title))
        self.wait(2)
        self.play(ReplacementTransform(title, expTitle))
        self.play(expTitle.animate.shift(UP), Write(defIvt))
        self.wait(2)
        self.play(FadeOut(defIvt), ReplacementTransform(expTitle, titleTopLeft), titleTopLeft.to_edge(UL, buff=0.5))
        self.play(Write(axes), Write(graph1))
        self.wait(2)