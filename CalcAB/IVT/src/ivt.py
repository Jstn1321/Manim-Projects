from manim import *

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
            x_range=[0, 3],
            y_range=[0, 5],
            axis_config = {"include_tip" : False}
        ).to_edge(DL, buff=0.5)

        graph1 = axes.plot(
            lambda x: x**2,
            stroke_color = BLUE,
            x_range=[0,2]
        )
        highlightGraph1 = axes.plot(
            lambda x: x**2,
            stroke_color = RED
        )

        dot0 = Dot(color=RED).move_to(axes.i2gp(0, graph1))
        dot2 = Dot(color=RED).move_to(axes.i2gp(2, graph1))

        title = Tex("The IVT")
        titleTopLeft = Tex("IVT").shift(UP)
        expTitle = Tex("The Intermediate Value Theorum")
        defIvt = Tex("If a continuous function changes from one value to another over an interval, it must take on every value in between").scale(0.8)
        givenFText = Tex("Given continuous function f(x) on the interval of [0, 2]:").to_edge(UP, buff=0.5)
        fexplain = Tex("This menas that because the functoin f is continous and has a value of both 0, 4, the function f must also have all the values between 0 and 4 aswell.").to_edge(RIGHT, buff=0.5)

        self.play(Write(title))
        self.wait(2)
        self.play(ReplacementTransform(title, expTitle))
        self.play(expTitle.animate.shift(UP), Write(defIvt))
        self.wait(7)
        self.play(FadeOut(defIvt), ReplacementTransform(expTitle, titleTopLeft))
        self.play(Write(givenFText))
        self.play(Write(tableOfF), titleTopLeft.animate.to_edge(UL, buff=0.5))
        self.wait(2)
        self.play(tableOfF.animate.to_edge(UR, buff=0.5), Write(graph1), Write(dot0), Write(dot2), Write(fexplain))
        self.wait(2)
        self.play(FadeIn(highlightGraph1))
        self.wait(2)