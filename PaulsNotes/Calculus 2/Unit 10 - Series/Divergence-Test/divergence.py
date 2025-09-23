from manim import *

class DivergenceTest(Scene):
    def construct(self):
        
        title = Tex("The Divergence Test")
        test = MathTex(r"\text{If} \lim_{n\to\infty} a_{n} \neq 0 \text{ then} \sum a_{n} \text{will diverge}")

        self.play(Write(title))
        self.wait(2)
        self.play(ReplacementTransform(title, test))
        self.wait(2)