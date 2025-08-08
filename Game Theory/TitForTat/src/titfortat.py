from manim import *
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
        firstStep = Tex("The first move is to cooperate").to_edge(UP, buff=1)
        secondStep = Tex("The next step is to copy each step the opponent makes").to_edge(UP, buff=1)
        p2FirstMoveText = Tex("If p2 refuses to cooperate...").to_edge(UP, buff=1)
        p1SecondMoveText = Tex("then p1 will copy his move!").to_edge(UP, buff=1)
        # Create the empty table first
        empty_values = [["" for _ in range(7)] for _ in range(2)]  # Create a blank table with the same dimensions
        empty_table = Table(
            table=empty_values,
            row_labels=[Text("p1"), Text("p2")],
            col_labels=[Text("1"), Text("2"), Text("3"), Text("4"), Text("5"), Text("6"), Text("7")],
            top_left_entry=Star().scale(0.3),
            include_outer_lines=True,
            arrange_in_grid_config={"cell_alignment": RIGHT}
        )
        firstfirstcell = empty_table.get_cell((2, 2))  
        p2FirstMove = empty_table.get_cell((3, 2))
        p1SecondMove = empty_table.get_cell((2,3))
        self.wait(1)
        self.play(Write(title))
        self.wait(1.5)
        self.play(title.animate.shift(UP*1.5))
        self.play(Write(titfortatDef))
        self.wait(6)
        self.play(ReplacementTransform(title, consider), ReplacementTransform(titfortatDef, empty_table))
        self.wait(1.5)
        self.play(ReplacementTransform(titfortatDef, Text("C").move_to(firstfirstcell.get_center())), ReplacementTransform(consider, firstStep))
        self.wait(2)
        self.play(ReplacementTransform(firstStep, secondStep))
        self.wait(3)
        self.play(ReplacementTransform(secondStep, p2FirstMoveText), Write(Text("D").move_to(p2FirstMove.get_center())))
        self.wait(4)
        self.play(ReplacementTransform(p2FirstMoveText, p1SecondMoveText), Write(Text("D").move_to(p1SecondMove.get_center())))
        self.wait(2)