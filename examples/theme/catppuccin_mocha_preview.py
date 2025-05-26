import manim
from manim import *

from manim_themes.manim_theme import apply_theme
from manim_themes.theme_preview import theme_preview


class CatppucinMochaPreview(Scene):

    def setup(self):
        theme = "catppuccin-mocha"
        apply_theme(manim_scene=self, theme_name=theme)



    def construct(self):
        my_theme_preview = theme_preview()
        self.add(my_theme_preview)


if __name__ == '__main__':
    import os
    from pathlib import Path

    FLAGS = "-pqm -s"
    SCENE = "CatppucinMochaPreview"

    file_path = Path(__file__).resolve()
    os.system(f"manim {Path(__file__).resolve()} {SCENE} {FLAGS}")

