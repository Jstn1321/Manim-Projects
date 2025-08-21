from manim import *

class sequences(Scene):
    def construct(self):
        classTitle = Tex("Calculus 2/BC").to_edge(UP, buff=1)
        title = Tex("Series").scale(2)

        self.play(Write(classTitle))
        self.play(Write(title))
        self.wait(2)