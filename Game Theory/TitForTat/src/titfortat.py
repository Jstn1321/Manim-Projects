from manim import *

# Example of writing only the first element of a list using Manim
class DisplayFirstElement(Scene):
    def construct(self):
        my_list = ["C", "D", "C", "D"]
        first_element = Text(my_list[0])  # Create a Text object with the first element
        self.play(Write(first_element))  # Animate writing the first element
        self.wait(2)  # Pause to display the result
class titfortat(Scene):
    def construct(self):
        values = [["C", "C", "D", "D", "C", "D", "C"],
             ["C", "D", "D", "C", "D", "C", "D"]]
        tableVal = Table(
            table=values,
             row_labels=[Text("p1"), Text("p2")],
             col_labels=[Text("1"), Text("2"), Text("3"), Text("4"), Text("5"), Text("6"), Text("7")],
             top_left_entry=Star().scale(0.3),
             include_outer_lines=True,
             arrange_in_grid_config={"cell_alignment": RIGHT}
        )

        title = Tex("Tit For Tat")
        titfortatDef = Tex("A highly effective strategy in game theory where an agent using this strategy will first cooperate, then subsequently replicate an opponent's previous action.").scale(0.8)
        consider = Tex("Consider the following prisoner dilemma game:").to_edge(UP, buff=1)
        firstStep = Tex("The first move is to cooperate then").to_edge(UP, buff=1)

        self.play(Write(title))
        self.wait(1.5)
        self.play(title.animate.shift(UP*1.5))
        self.play(Write(titfortatDef))
        self.wait(6)
        self.play(title.animate.to_edge(UP, buff=1), ReplacementTransform(titfortatDef, Write(Text(Group(values[0][0], values[1][0])))))
        self.wait(1.5)
