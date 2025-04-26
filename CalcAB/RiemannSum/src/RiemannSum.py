from manim import *
import math

class RiemannSum(Scene):
    def construct(self):
        
        axes = Axes(
            x_range=[-1, 5],
            y_range=[-1, 5],
            y_length=5,
            axis_config={"color": WHITE, "include_tip": False},
        ).to_edge(DL, buff=0.5).add_coordinates()

        func = axes.plot(
            lambda x: -0.19 * pow(x,3) + pow(x,2),
            color = WHITE,
            x_range=[-1,5]
        )

        func_label = MathTex(r"-0.19x^3 + x^2").next_to(axes.i2gp(3.5, func), UP)

        title = Tex("The Integral")
        # 0 + 0.81 + 2.48 + 3.87 + 3.84
        finiteSumForm = MathTex(r"\sum_{i = 1}^{5}-0.19x_{i}^3 + x_{i}^2")
        finiteSumForm.to_edge(UP, buff=1)
        sumdx1 = MathTex(r" = (0 \times 1) + (0.81 \times 1) + (2.48 \times 1) + (3.87 \times 1) + (3.84 \times 1)")
        sumdx1.to_edge(UP, buff=1)
        resultSumDx1 = MathTex(r"\sum_{i = 1}^{5}-0.19x_{i}^3 + x_{i}^2 = 11")
        resultSumDx1.to_edge(UP, buff=1)
        sumEq = MathTex(r"\sum_{i = 1}^{\infty}-0.19x_{i}^3 + x_{i}^2")
        sumEq.to_edge(UP, buff=1)
        approx11 = MathTex(r" \approx 11.94")
        approx11.to_edge(UP, buff=1.5)
        sumEq.to_edge(UP, buff=1)
        intgralNot = MathTex(r"\int_{0}^{5} -0.19x^3+x^2 \,dx")
        intgralNot.to_edge(UP, buff=1)
        antiDervUnsimp = MathTex(r"\int_{0}^{5} -0.19x^3+x^2 \,dx = \frac{-0.19}{4}x^4 + \frac{1}{3}x^3 \big|_0^5")
        antiDervUnsimp.to_edge(UP, buff=1)
        antiDervUnsimp2 = MathTex(r"= ((\frac{-0.19}{4})(5^4) + (\frac{1}{3})(5^3)) - 0")
        antiDervUnsimp2.to_edge(UP, buff=1)
        antiDervSimp = MathTex(r"\int_{0}^{5} -0.19x^3+x^2 \,dx \approx 11.9791667")
        antiDervSimp.to_edge(UP,buff=1)
        riemanDef = MathTex(r"\sum_{i = 1}^{\infty}f(x_i)\Delta x_i")
        standInte = MathTex(r"\int_{a}^{b}f(x) \,dx")
        ftc = MathTex(r"\int_{a}^{b}f(x) \,dx = F(b) - F(a)\big|_{a}^{b}")
        finalText = Tex("The Integral")

        dx = ValueTracker(1)

        rieman_rect = always_redraw(lambda: 
            axes.get_riemann_rectangles(
                graph=func,
                x_range=[0, 4.99],
                dx=max(dx.get_value(), 0.01), #Change back to 0.01
                stroke_color=BLUE,
                input_sample_type="left",
                fill_opacity=0.75
            )
        )
        area_func = axes.get_area(graph=func, x_range=[0,5], color=BLUE, opacity=0.75)


        self.play(Write(title), run_time = 2)
        self.wait(1.5)
        self.play(title.animate.to_edge(UP, buff=1))
        self.play(Write(axes), Create(func), Write(func_label))
        self.play(Create(rieman_rect))
        self.play(ReplacementTransform(title, finiteSumForm))
        self.wait(3)
        self.play(ReplacementTransform(finiteSumForm, sumdx1))
        self.wait(3)
        self.play(ReplacementTransform(sumdx1, resultSumDx1))
        self.wait(3)
        self.play(ReplacementTransform(resultSumDx1, sumEq), run_time = 1)
        self.play(dx.animate.set_value(0.01), run_time=10)#Change back to 0.01
        self.wait(3)
        self.add(approx11)
        self.play(sumEq.animate.shift(LEFT*1), approx11.animate.shift(RIGHT*2))
        self.wait(3)
        self.remove(approx11)
        self.play(FadeTransform(rieman_rect, area_func),ReplacementTransform(sumEq, intgralNot), run_time=1)
        self.wait(3)
        self.play(ReplacementTransform(intgralNot, antiDervUnsimp))
        self.wait(3)
        self.play(ReplacementTransform(antiDervUnsimp, antiDervUnsimp2))
        self.wait(3)
        self.play(ReplacementTransform(antiDervUnsimp2, antiDervSimp))
        self.wait(3)
        self.play(FadeOut(Group(axes,func,func_label,area_func)), ReplacementTransform(antiDervSimp, riemanDef), run_time = 2)
        self.wait(1)
        self.play(ReplacementTransform(riemanDef, standInte))
        self.wait(2)
        self.play(ReplacementTransform(standInte, ftc))
        self.wait(2)
        self.play(ReplacementTransform(ftc, finalText))
        self.wait(2)
        self.play(Unwrite(finalText), run_time = 4)