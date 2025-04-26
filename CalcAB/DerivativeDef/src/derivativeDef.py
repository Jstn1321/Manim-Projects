from manim import *
import math
#manim -pqh derivativeDef.py DerivativeDef
class DerivativeDef(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-5, 5], 
            y_range=[-1, 4],
            y_length=5,
            x_length=10,
            axis_config={"color": WHITE, "include_tip": False, "include_numbers": True},
        ).to_edge(DOWN)
        axes.add_coordinates()

        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        func = axes.plot(
            lambda x: 0.2 * x * x,  
            stroke_color=BLUE,
            x_range=[-5,5,0.001]     
        )

        func_label = MathTex(r"0.2x^2").next_to(axes.i2gp(5, func), LEFT)

        title = Tex("The Derivative")        

        self.play(Write(title), runtime = 4)
        self.wait(1.5)
        self.play(title.animate.to_edge(UP, buff=0.60))
        self.play(Write(axes), Write(axes_labels), run_time = 2)
        self.play(Create(func, run_time=2))
        self.play(Write(func_label))
        self.wait()

        dota = Dot(color = RED)
        dota.move_to(axes.i2gp(1, func))
        self.play(FadeIn(dota,scale=0.5))

        dotb = Dot(color = RED)
        dotb.move_to(axes.i2gp(4, func))
        self.play(FadeIn(dotb,scale=0.5))

        dotb_tracker = ValueTracker(4)
        f_always(
            dotb.move_to,
            lambda: axes.i2gp(dotb_tracker.get_value(), func)
        )

        
        dx = ValueTracker(3)
        x = ValueTracker(1)

        derv = always_redraw(lambda : axes.get_secant_slope_group(graph = func, x = x.get_value(),dx = dx.get_value(), secant_line_color=PURPLE, dy_line_color= YELLOW, dx_line_color=GREEN, secant_line_length=8, dx_label="h", dy_label="f(x+h)-f(x)"))

        f_always(
            dota.move_to,
            lambda: axes.i2gp(x.get_value(), func)
        )
        
        slopeText = MathTex(r"slope = \frac{f(b)-f(a)}{b-a}")
        slopeText.to_edge(UP, buff=0.6)
        self.play(Create(derv), ReplacementTransform(title, slopeText))
        self.wait(2)
        dervDef = MathTex(r"\lim_{h \to 0} f(x) = \frac{f(x + h) - f(x)}{h}")
        dervDef.to_edge(UP, buff=0.6)
        self.play(ReplacementTransform(slopeText, dervDef))
        self.play(dx.animate.set_value(0.01),dotb_tracker.animate.set_value(1), run_time = 8)
        self.wait()
        self.remove(dotb)
        fprimeUnSimp = MathTex(r"f'(x) = \frac{d}{dx}(0.2x^2)")
        fprimeUnSimp.to_edge(UP, buff=0.6)
        self.play(ReplacementTransform(dervDef, fprimeUnSimp))
        self.wait(1)
        fprime = MathTex(r"f'(x) = 0.4x")
        fprime.to_edge(UP, buff=0.6)
        self.play(ReplacementTransform(fprimeUnSimp, fprime))
        self.wait(1)
        def create_fprime_val():
            x_val = x.get_value()
            group = VGroup(
                MathTex("f'("),
                DecimalNumber(x_val, num_decimal_places=3),
                MathTex(") = "),
                DecimalNumber(0.4*x_val, num_decimal_places=3)
            ).arrange(RIGHT).to_edge(UP, buff=0.6)
            return group

        fprimeVal = always_redraw(create_fprime_val)
        self.play(ReplacementTransform(fprime, fprimeVal))
        self.play(x.animate.set_value(-3), run_time = 4)
        self.wait()
        self.play(x.animate.move_to(3), run_time = 4)
        self.wait(1)
        dotb.clear_updaters()
        dota.clear_updaters()
        fprimeVal.clear_updaters()
        derv.clear_updaters()

        final_derv_def = MathTex(r"\lim_{h \to 0} f(x) = \frac{f(x + h) - f(x)}{h}")
        eulerFormat = MathTex(r"D(f(x))")
        newtonFormat = MathTex(r"\dot y")
        leibnizFormat = MathTex(r"\frac{dy}{dx}")
        lagrangeFormat = MathTex(r"f'(x)")
        final_text = Tex("The Derivative")

        self.play(
            FadeOut(Group(axes, axes_labels, func, func_label, fprimeVal, dota, derv)),
            #final_derv_def.animate.set_opacity(1),
            run_time=2
        )
        self.play(FadeIn(final_derv_def),run_time = 1)
        self.play(ReplacementTransform(final_derv_def, eulerFormat))
        self.wait(0.5)
        self.play(ReplacementTransform(eulerFormat, newtonFormat))
        self.wait(0.5)
        self.play(ReplacementTransform(newtonFormat, leibnizFormat))
        self.wait(0.5)
        self.play(ReplacementTransform(leibnizFormat, lagrangeFormat))
        self.wait(0.5)
        self.play(ReplacementTransform(lagrangeFormat, final_text))
        self.wait(1)
        self.play(FadeOut(final_text), run_time = 3)