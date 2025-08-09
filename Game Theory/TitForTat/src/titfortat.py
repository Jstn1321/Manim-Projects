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
        p1SecondMoveText = Tex("then p1 will also refuse to cooperate!").to_edge(UP, buff=1)
        p2SecondMoveText = Tex("If p2 wants to cooperate...").to_edge(UP, buff=1)
        p1ThirdMoveText = Tex("then p1 will also cooperate!").to_edge(UP, buff=1)
        p1RestofGameText = Tex("After the first move p1 will copy whatever move p2 makes").to_edge(UP, buff=1)
        finalText = Tex("TitforTat is an extremely effective strategy because it is: ").to_edge(UL, buff=0.3)
        
        factorsOfTitforTat = BulletedList(
            "Clear - it is simple allowing other players to understand it",
            "Nice - it begins with cooperation and only defects if the other player defects",
            "Provocable - can defect if the opponent wants to defect",
            "Forgiving - cooperates if the other player cooperates and dosen't hold grudges",
        ).next_to(finalText, DOWN, buff=1).scale(0.8).shift(RIGHT*0.5)
        
        #factorsOfTitforTat = BulletedList("Item 1adwadadwa d", "Item 2", "Item 3")
        # Create the empty table first
        empty_values = [["" for _ in range(7)] for _ in range(2)]
        empty_table = Table(
            table=empty_values,
            row_labels=[Text("p1"), Text("p2")],
            col_labels=[Text("1"), Text("2"), Text("3"), Text("4"), Text("5"), Text("6"), Text("7")],
            top_left_entry=Star().scale(0.3),
            include_outer_lines=True,
            arrange_in_grid_config={"cell_alignment": RIGHT}
        )
        
        # Store references to all the move texts
        move_texts = []
        
        self.wait(1)
        self.play(Write(title))
        self.wait(1.5)
        self.play(title.animate.shift(UP*1.5))
        self.play(Write(titfortatDef))
        self.wait(6)
        self.play(ReplacementTransform(title, consider), ReplacementTransform(titfortatDef, empty_table))
        self.wait(1.5)
        
        # First move
        p1_first_text = Text("C").move_to(empty_table.get_cell((2, 2)).get_center())
        move_texts.append(p1_first_text)
        self.play(Write(p1_first_text), ReplacementTransform(consider, firstStep))
        self.wait(2)
        self.play(ReplacementTransform(firstStep, secondStep))
        self.wait(3)
        
        # Second move
        p2_first_text = Text("D").move_to(empty_table.get_cell((3, 2)).get_center())
        move_texts.append(p2_first_text)
        self.play(Write(p2_first_text), ReplacementTransform(secondStep, p2FirstMoveText))
        self.wait(4)
        
        # Third move
        p1_second_text = Text("D").move_to(empty_table.get_cell((2, 3)).get_center())
        move_texts.append(p1_second_text)
        self.play(Write(p1_second_text), ReplacementTransform(p2FirstMoveText, p1SecondMoveText))
        self.wait(2)
        
        # Fourth move
        p2_second_text = Text("C").move_to(empty_table.get_cell((3, 3)).get_center())
        move_texts.append(p2_second_text)
        self.play(Write(p2_second_text), ReplacementTransform(p1SecondMoveText, p2SecondMoveText))
        self.wait(4)
        
        # Fifth move
        p1_third_text = Text("C").move_to(empty_table.get_cell((2, 4)).get_center())
        move_texts.append(p1_third_text)
        self.play(Write(p1_third_text), ReplacementTransform(p2SecondMoveText, p1ThirdMoveText))
        self.wait(2)
        
        # Remaining moves
        remaining_texts = [
            Text("C").move_to(empty_table.get_cell((3, 4)).get_center()),
            Text("C").move_to(empty_table.get_cell((2, 5)).get_center()),
            Text("D").move_to(empty_table.get_cell((3, 5)).get_center()),
            Text("D").move_to(empty_table.get_cell((2, 6)).get_center()),
            Text("D").move_to(empty_table.get_cell((3, 6)).get_center()),
            Text("D").move_to(empty_table.get_cell((2, 7)).get_center()),
            Text("C").move_to(empty_table.get_cell((3, 7)).get_center()),
            Text("C").move_to(empty_table.get_cell((2, 8)).get_center()),
            Text("D").move_to(empty_table.get_cell((3, 8)).get_center())
        ]
        move_texts.extend(remaining_texts)
        self.play(*[Write(t) for t in remaining_texts], ReplacementTransform(p1ThirdMoveText, p1RestofGameText))
        self.wait(7)
        
        # Final transition
        self.play(
            FadeOut(empty_table),
            *[FadeOut(t) for t in move_texts],
            ReplacementTransform(p1RestofGameText, finalText)
        )
        self.play(Write(factorsOfTitforTat))
        self.wait(10)