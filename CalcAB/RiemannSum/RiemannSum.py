from manim import *
import math

class RiemannSum(Scene):
    def construct(self):
        
        axes = Axes(
            x_range=[-1, 5],
            y_range=[-1, 5],
            axis_config={"color": WHITE, "include_tip": False},
        ).to_edge(DL, buff=0.5).add_coordinates()

        func = axes.plot(
            lambda x: -0.19 * pow(x,3) + pow(x,2),
            color = WHITE,
            x_range=[-1,5]
        )

        title = Tex("The Integral")
        # 0 + 0.81 + 2.48 + 3.87 + 3.84
        sumdx1 = MathTex(r"(0 * 1) + (0.81 * 1) + (2.48 * 1) + (3.87 * 1) + (3.84 * 1)")
        sumdx1.to_edge(UP, buff=1)

        dx = ValueTracker(1)

        rieman_rect = always_redraw(lambda: 
            axes.get_riemann_rectangles(
                graph=func,
                x_range=[0, 4.99],
                dx=max(dx.get_value(), 0.1), #Change back to 0.01
                stroke_color=BLUE,
                input_sample_type="left",
                fill_opacity=0.75
            )
        )
        area_func = axes.get_area(graph=func, x_range=[0,5], color=BLUE, opacity=0.75)


        self.play(Write(title), run_time = 2)
        self.wait(1.5)
        self.play(title.animate.to_edge(UP, buff=1))
        self.play(Write(axes), Create(func))
        self.play(Create(rieman_rect))
        self.play(ReplacementTransform(title, sumdx1))
        self.wait(1.5)
        self.play(dx.animate.set_value(0.1), run_time=10)#Change back to 0.01
        self.wait()
        self.play(FadeOut(rieman_rect), FadeIn(area_func),run_time=1)


        