from manim import *


class GraphDemo(Scene):
    def construct(self):
        node_a = Circle(radius=0.5, color=BLUE).shift(LEFT * 2)
        node_b = Circle(radius=0.5, color=GREEN).shift(RIGHT * 2)
        arrow = Arrow(node_a.get_right(), node_b.get_left())

        self.play(Create(node_a), Create(node_b))
        self.play(GrowArrow(arrow))
        self.wait(1)
