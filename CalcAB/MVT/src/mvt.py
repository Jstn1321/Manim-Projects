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
            lambda x: -1 * (x)**3 + 3*x**2 + x,
            stroke_color = BLUE
        )

        avgSlope = axes.plot(
            lambda x: x,
            stroke_color = GREEN,
            x_range=[-1, 4]
        )

        x = ValueTracker(0) #Go up till x = 2
        derv = always_redraw(lambda: axes.get_secant_slope_group(graph=func, x = x.get_value(), dx = 0.01, secant_line_length=10, secant_line_color=YELLOW))
        dotA = Dot(color=PURE_RED).move_to(axes.i2gp(0, avgSlope))
        dotB = Dot(color=PURE_RED).move_to(axes.i2gp(3, avgSlope))

        mvtAb = Text(r"The MVT")
        mvtExp = Text(r"The Mean Value Theorum")
        mvtDef = Text("For a continuous and differentiable function, there exists \n a point where the derivative equals the average \n rate of change over an interval").scale(0.8)
        mvtAbP2 = Text(r"The MVT").shift(UP*1.5)
        avgSlopeLabel  = MathTex(r"Slope = \frac{y_{2}-y_{1}}{x_{2}-x_{1}} = 1").next_to(axes.i2gp(2, avgSlope), DOWN*1.3)
        dervLabel = MathTex(r"f'(2) = 1").next_to(axes.i2gp(2, func), DOWN*1.5)
        slopeeqdervlabel = MathTex(r"\frac{y_{2}-y_{1}}{x_{2}-x_{1}} = f'(c)")
        finalText = Tex("The Mean Value Theorum")

        self.play(Write(mvtAb))
        self.wait(1.5)
        self.play(ReplacementTransform(mvtAb, mvtExp))
        self.wait(1.5)
        self.play(mvtExp.animate.shift(UP*1.5), Write(mvtDef))
        self.wait(6)
        self.play(ReplacementTransform(mvtExp, mvtAbP2), FadeOut(mvtDef))
        self.play(mvtAbP2.animate.to_edge(UP, buff=1), Write(axes), Write(axes_label), Write(func))
        self.wait(1.5)
        self.play(Write(avgSlope), Create(dotA), Create(dotB))
        self.wait(1.5)
        self.play(Write(avgSlopeLabel))
        self.wait(1.5)
        self.play(Write(derv))
        self.play(x.animate.set_value(2), run_time = 6)
        self.wait(1.5)
        self.play(Write(dervLabel))
        self.wait(1.5)
        self.play(ReplacementTransform(Group(avgSlopeLabel, dervLabel), slopeeqdervlabel), FadeOut(axes, axes_label, func, avgSlope, mvtAbP2, dotA, dotB, derv))
        self.wait(1.5)
        self.play(ReplacementTransform(slopeeqdervlabel, finalText))
        self.wait(1.5)
        self.play(Unwrite(finalText))
        self.wait()