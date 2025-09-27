from manim import *

class PSeries(Scene):
    def construct(self):

        test = MathTex(r"\text{If k > 0 then } \sum_{n=k}^{\infty} \frac{1}{n^{p}} \text{ converges if p > 1 and diverges if p ≤ 1}")
        example1 = MathTex(r"\sum_{n=4}^{\infty}\frac{1}{n^{7}}")
        example2 = MathTex(r"\sum_{n=1}^{\infty}\frac{1}{n^{\frac{1}{\sqrt{n}}}}")

        self.play(Write(Text("P-Series Test")))