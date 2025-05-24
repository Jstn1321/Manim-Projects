from manim import *
import math

class ivt(Scene):
    def construct(self):
        tableOfFVal = [["0", "?", "4"], ["0", "1", "2"]]
        tableOfF = Table(
            table=tableOfFVal,
            row_labels=[Text("f(x)"), Text("x")],
            col_labels=None,
            include_outer_lines=True,
            arrange_in_grid_config={"cell_alignment": RIGHT}
        )

        axes = Axes(
            x_range=[-0.5, 3],
            y_range=[-0.5, 5],
            axis_config = {"include_tip" : False}
        ).to_edge(DL, buff=0.5)

        graph1 = axes.plot(
            lambda x: 2*x,
            stroke_color = BLUE,
            x_range=[0,2]
        )

        graph2 = axes.plot(
            lambda x: x**2,
            stroke_color = GREEN,
            x_range=[0,2]
        )

        graph3 = axes.plot(
            lambda x: (4/math.log(3))*math.log(x+1),
            stroke_color = PURPLE,
            x_range=[0,2]
        )

        dot0 = Dot(color=RED).move_to(axes.i2gp(0, graph1))
        dot2 = Dot(color=RED).move_to(axes.i2gp(2, graph1))

        title = Tex("The IVT")
        expTitle = Tex("The Intermediate Value Theorum")
        defIvt = Tex("If a continuous function changes from one value to another over an interval, it must take on every value in between").scale(0.8)
        givenFText = Tex("Given continuous function f(x) on the interval of [0, 2]:").to_edge(UP, buff=0.5)
        fexplain = Tex("This means that because the function f is continous and has a value of both 0 and 4, the function f must also have all the values between 0 and 4 aswell.").scale(0.8).to_edge(RIGHT, buff=0.5).shift(DOWN)
        graphExpP1 = Tex("No matter what type of function,").next_to(axes.i2gp(2, graph3), DOWN*7)
        graphExpP2 = Tex("the values of f between the").next_to(axes.i2gp(2, graph3), DOWN*9)
        graphExpP3 = Tex("intervals must be between 0 and 4").next_to(axes.i2gp(2, graph3), DOWN*11)
        finalIVTexp = Tex("The Intermediate Value Theorum")
        finalTex = Tex("The IVT")

        self.play(Write(title))
        self.wait(2)
        self.play(ReplacementTransform(title, expTitle))
        self.play(expTitle.animate.shift(UP), Write(defIvt))
        self.wait(7)
        self.play(FadeOut(defIvt), FadeOut(defIvt), Write(tableOfF), Write(givenFText),FadeOut(expTitle))
        self.wait(2)
        self.play(Write(fexplain), tableOfF.animate.shift(UP))
        self.wait(7)
        self.play(FadeOut(Group(fexplain, tableOfF)))
        self.play(Write(dot0), Write(dot2), Write(axes))
        self.wait(5)
        self.play(FadeIn(graph1))
        self.wait(2),
        self.play(ReplacementTransform(graph1, graph2))
        self.wait(2)
        self.play(ReplacementTransform(graph2, graph3))
        self.wait(2)
        self.play(Write(graphExpP1))
        self.play(Write(graphExpP2))
        self.play(Write(graphExpP3))
        self.wait(4)
        self.play(FadeOut(Group(axes, givenFText, graph3, dot0, dot2, graphExpP1, graphExpP2, graphExpP3)))
        self.play(Write(finalIVTexp))
        self.wait(1.5)
        self.play(ReplacementTransform(finalIVTexp, finalTex))
        self.wait(1.5)
        self.play(Unwrite(finalTex), run_time = 5)