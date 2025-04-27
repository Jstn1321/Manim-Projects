from manim import *

class TaylorSeries(Scene):
    def construct(self):
        axes = Axes(
            x_range = [-10, 10],
            y_range = [-5, 5],
            y_length=5.5,
            axis_config={"include_tip": False}
        ).to_edge(DOWN, buff=0.5)

        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

        title = Tex("The Taylor Series")
        expandTaylorSeries = MathTex(r"f(a) + \frac{f'(a)}{1!}(x - a) + \frac{f''(a)}{2!}(x-a)^2 + ...").to_edge(UP, buff=0.5)
        fullExpandSeries = MathTex(r"f(a) + \frac{f'(a)}{1!}(x - a) + \frac{f''(a)}{2!}(x-a)^2 + ... = \sum_{n = 0}^{\infty}\frac{f^(n)(a)}{n!}(x - a)^n").to_edge(UP, buff=0.5)
        
        
        
        func = axes.plot(
            lambda x: np.sin(x),
            stroke_color = BLUE
        )

        self.play(Write(title))
        self.wait(1.5)
        self.play(title.animate.to_edge(UP, buff=1), Write(axes), Write(axes_labels), Write(func))
        self.play(ReplacementTransform(title, expandTaylorSeries))
        self.wait(2)
        self.play(ReplacementTransform(expandTaylorSeries, fullExpandSeries))
