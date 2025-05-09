from manim import *

class evt(Scene):
    def construct(self):
        title = Tex("The Extreme Value Theorum")
        evtDef = Tex("a continuous function defined on a closed interval will always have both a maximum and a minimum value within that interval.").scale(0.8)
        ex1Text = Tex("Ex 1: ").to_edge(UL, buff=0.5)
        ex2Text = Tex("Ex 2: ").to_edge(UL, buff=0.5)
        fHasMaxAtTex = Tex("f(x) has a abs max at: ").to_edge(UP, buff=0.5).shift(LEFT)
        fHasMinAtTex = Tex("and a abs min at: ").to_edge(UP, buff=1).shift(LEFT*0.5)
        func1Max = MathTex(r"x = 0.75").to_edge(UP, buff=0.5).shift(RIGHT*2.5)
        func1Min = MathTex(r"x = 1.57").to_edge(UP, buff=1).shift(RIGHT*2.5)

        gHasMaxAtTex = Tex("g(x) has a abs max at: ").to_edge(UP, buff=0.5).shift(LEFT)
        gHasMinAtTex = Tex("and a abs min at: ").to_edge(UP, buff=1).shift(LEFT*0.5)
        func2Max = MathTex(r"x = 1.3").to_edge(UP, buff=0.5).shift(RIGHT*2.5)
        func2Min = MathTex(r"x = 4").to_edge(UP, buff=1).shift(RIGHT*2.5)

        finalText = Tex("The Extreme Value Theorum")
        
        axes = Axes(
            x_range = [0, 4],
            y_range = [0, 10],
            axis_config={"include_tip": False, "include_numbers": False}
        ).to_edge(DL, buff=0.5)

        func1 = axes.plot(
            lambda x: ((x-4)**4) + (4*(x-4)**3) + (3*(x-4)**2) + (x-4) + 8,
            stroke_color = BLUE,
            x_range=[0.75, 4]
        )
        func1_label = MathTex(r"f(x)").next_to(axes.i2gp(2, func1), RIGHT)

        func1MaxDot = Dot(color=RED).move_to(axes.i2gp(0.75, func1))
        func1MinDot = Dot(color=RED).move_to(axes.i2gp(1.57634, func1))


        func2 = axes.plot(
            lambda x: np.e**np.sin(x) * np.sinh(x)-3,
            stroke_color = RED,
            x_range=[1.3, 4]
        )
        func2_label = MathTex(r"g(x)").next_to(axes.i2gp(2, func2), RIGHT)

        func2MaxDot = Dot(color=BLUE).move_to(axes.i2gp(4, func2))
        func2MinDot = Dot(color=BLUE).move_to(axes.i2gp(1.3, func2))
        
        self.play(Write(title))
        self.wait(2)
        self.play(title.animate.shift(UP), Write(evtDef))
        self.wait(5)
        self.play(ReplacementTransform(title, ex1Text), FadeOut(evtDef))
        self.play(Write(axes), Write(func1), Write(func1_label))
        self.wait(2)
        self.play(Write(fHasMaxAtTex), Write(fHasMinAtTex))
        self.wait(2)
        self.play(Write(func1Max), Write(func1Min), Create(func1MaxDot), Create(func1MinDot))
        self.wait(3)
        self.play(ReplacementTransform(ex1Text, ex2Text), FadeOut(Group(func1MaxDot, func1MinDot, fHasMaxAtTex, fHasMinAtTex, func1Max, func1Min)), ReplacementTransform(func1, func2), ReplacementTransform(func1_label, func2_label))
        self.wait(1)
        self.play(Write(gHasMaxAtTex), Write(gHasMinAtTex))
        self.wait(2)
        self.play(Write(func2Max), Write(func2Min), Create(func2MaxDot), Create(func2MinDot))
        self.wait(3)
        self.play(FadeOut(Group(func2MaxDot, func2MinDot, gHasMaxAtTex, gHasMinAtTex, func2Min, func2Max, ex2Text, func2_label)), ReplacementTransform(Group(func2, axes), finalText))
        self.wait(2)
        self.play(Unwrite(finalText), run_time = 2)