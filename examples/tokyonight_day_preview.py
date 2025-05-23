import manim
from manim import *

from manim_themes.manim_theme import apply_theme
from manim_themes.theme_preview import theme_preview


class TokyonightDayPreview(Scene):

    def setup(self):
        theme = "tokyonight-day"
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True)


    def construct(self):
        my_theme = theme_preview()
        self.add(my_theme)


if __name__ == '__main__':
    import os
    from pathlib import Path

    FLAGS = "-pqm -s"
    SCENE = "TokyonightDayPreview"

    file_path = Path(__file__).resolve()
    os.system(f"manim {Path(__file__).resolve()} {SCENE} {FLAGS}")

