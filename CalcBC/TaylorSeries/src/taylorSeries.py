from manim import *
import math

class TaylorSeries(Scene):
    def construct(self):
        axes = Axes(
            x_range = [-10, 10],
            y_range = [-5, 5],
            y_length=5.5,
            axis_config={"include_tip": False}
        ).to_edge(DOWN, buff=0.5)

        title = Tex("The Taylor Series")
        expandTaylorSeries = MathTex(r"f(a) + \frac{f'(a)}{1!}(x - a) + \frac{f''(a)}{2!}(x-a)^2 + ...").to_edge(UP, buff=0.5)
        fullExpandSeries = MathTex(r" = \sum_{n = 0}^{\infty}\frac{f^{(n)}(a)}{n!}(x - a)^n").to_edge(UP, buff=0.5)
        taylor1Tex = MathTex(r"sin(x) \approx \sum_{n = 0}^{1}\frac{(-1)^n}{(2n+1)!}x^{2n+1}").to_edge(UP, buff=0.5)
        taylor5Tex = MathTex(r"sin(x) \approx \sum_{n = 0}^{5}\frac{(-1)^n}{(2n+1)!}x^{2n+1}").to_edge(UP, buff=0.5)
        taylor10Tex = MathTex(r"sin(x) \approx \sum_{n = 0}^{10}\frac{(-1)^n}{(2n+1)!}x^{2n+1}").to_edge(UP, buff=0.5)
        taylorInfTex = MathTex(r"sin(x) = \sum_{n = 0}^{\infty}\frac{(-1)^n}{(2n+1)!}x^{2n+1}").to_edge(UP, buff=0.5)
        mclarinSeries = MathTex(r"\sum_{n = 0}^{\infty}\frac{f^n(0)}{n!}x^n")

        def taylorSeries(x, n):
            sum = 0
            taylorUnsimp = []
            for i in range(n):
                taylorUnsimp.append(((-1)**i / math.factorial(2*i + 1)) * x**(2*i + 1))
            for i in range(n):
                sum += taylorUnsimp[i]
            return sum

        func = axes.plot(
            lambda x: np.sin(x),
            stroke_color = BLUE
        )
        func_label = MathTex(r"sin(x)").next_to(axes.i2gp(8, func), UP)

        taylor1 = axes.plot(lambda x: taylorSeries(x, 1), stroke_color = PURE_RED)
        taylor5 = axes.plot(lambda x: taylorSeries(x, 5), stroke_color = PURE_RED)
        taylor10 = axes.plot(lambda x: taylorSeries(x, 10), stroke_color = PURE_RED)
        finalFunc = axes.plot(
            lambda x: np.sin(x),
            stroke_color = PURE_RED
        )

        self.play(Write(title))
        self.wait(1.5) 
        self.play(title.animate.to_edge(UP, buff=1), Write(axes), Write(func), Write(func_label))
        self.play(ReplacementTransform(title, expandTaylorSeries))
        self.wait(2)
        self.play(ReplacementTransform(expandTaylorSeries, fullExpandSeries))
        self.wait(2)
        self.play(Write(taylor1), ReplacementTransform(fullExpandSeries, taylor1Tex))
        self.wait(1.5)
        self.play(ReplacementTransform(taylor1, taylor5), ReplacementTransform(taylor1Tex, taylor5Tex))
        self.wait(1.5)
        self.play(ReplacementTransform(taylor5, taylor10), ReplacementTransform(taylor5Tex, taylor10Tex))
        self.wait(1.5)
        self.play(ReplacementTransform(taylor10, finalFunc), ReplacementTransform(taylor10Tex, taylorInfTex))
        self.wait(1.5)
        self.play(FadeOut(Group(axes, func, func_label, finalFunc)), ReplacementTransform(taylorInfTex, mclarinSeries), run_time = 2)
        self.wait(1.5)