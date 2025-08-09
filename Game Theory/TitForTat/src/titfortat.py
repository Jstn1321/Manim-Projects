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
        p1SecondMoveText = Tex("then p1 will also defect!").to_edge(UP, buff=1)
        p2SecondMoveText = Tex("If p2 wants to cooperate...").to_edge(UP, buff=1)
        p1ThirdMoveText = Tex("then p1 will also cooperate!").to_edge(UP, buff=1)
        p1RestofGameText = Tex("After the first move p1 will copy what ever move p2 makes").to_edge(UP, buff=1)
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
        p1FirstMove = empty_table.get_cell((2, 2))  
        p1SecondMove = empty_table.get_cell((2,3))
        p1ThirdMove = empty_table.get_cell((2, 4))
        p1FourthMove = empty_table.get_cell((2, 5))
        p1fifthMove = empty_table.get_cell((2, 6))
        p1SixthMove = empty_table.get_cell((2, 7))
        p1SeventhMove = empty_table.get_cell((2, 8))
        p2FirstMove = empty_table.get_cell((3, 2))
        p2SecondMove = empty_table.get_cell((3, 3))
        p2ThirdMove = empty_table.get_cell((3, 4))
        p2FourthMove = empty_table.get_cell((3, 5))
        p2FifthMove = empty_table.get_cell((3, 6))
        p2SixthMove = empty_table.get_cell((3, 7))
        p2SeventhMove = empty_table.get_cell((3, 8))
        
        self.wait(1)
        self.play(Write(title))
        self.wait(1.5)
        self.play(title.animate.shift(UP*1.5))
        self.play(Write(titfortatDef))
        self.wait(6)
        self.play(ReplacementTransform(title, consider), ReplacementTransform(titfortatDef, empty_table))
        self.wait(1.5)
        self.play(ReplacementTransform(titfortatDef, Text("C").move_to(p1FirstMove.get_center())), ReplacementTransform(consider, firstStep))
        self.wait(2)
        self.play(ReplacementTransform(firstStep, secondStep))
        self.wait(3)
        self.play(ReplacementTransform(secondStep, p2FirstMoveText), Write(Text("D").move_to(p2FirstMove.get_center())))
        self.wait(4)
        self.play(ReplacementTransform(p2FirstMoveText, p1SecondMoveText), Write(Text("D").move_to(p1SecondMove.get_center())))
        self.wait(2)
        self.play(ReplacementTransform(p1SecondMoveText, p2SecondMoveText), Write(Text("C").move_to(p2SecondMove.get_center())))
        self.wait(4)
        self.play(ReplacementTransform(p2SecondMoveText, p1ThirdMoveText), Write(Text("C").move_to(p1ThirdMove.get_center())))
        self.wait(2)
        self.play(Write(Text("C").move_to(p2ThirdMove.get_center())), Write(Text("C").move_to(p1FourthMove.get_center())), Write(Text("D").move_to(p2FourthMove.get_center())), Write(Text("D").move_to(p1fifthMove.get_center())), Write(Text("D").move_to(p2FifthMove.get_center())), Write(Text("D").move_to(p1SixthMove.get_center())), Write(Text("C").move_to(p2SixthMove.get_center())), Write(Text("C").move_to(p1SeventhMove.get_center())), Write(Text("D").move_to(p2SeventhMove.get_center())), ReplacementTransform(p1ThirdMoveText, p1RestofGameText))
        self.wait(7)