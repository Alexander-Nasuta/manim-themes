import manim
from manim import *

from manim_themes.manim_theme import apply_theme


class BlazerExample(Scene):

    def setup(self):
        # Set the background color to a light beige
        theme = "tokyonight-day"
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True)

    def construct(self):
        my_text = Text("Hello World")
        red_text = Text("Red Text", color=RED)
        red_text.next_to(my_text, DOWN)

        self.play(
            FadeIn(my_text),
            FadeIn(red_text),
        )


if __name__ == '__main__':
    import os
    from pathlib import Path

    FLAGS = "-pqm"
    SCENE = "NerdfontIconOverview"

    file_path = Path(__file__).resolve()
    os.system(f"manim {Path(__file__).resolve()} {SCENE} {FLAGS}")

