import manim as m

from manim_themes.manim_theme import apply_theme
from manim_themes.theme_preview import theme_preview


class CatppucinLattePreview(m.Scene):

    def setup(self):
        theme = "catppuccin-latte"
        # add light_theme=True to change the default text color to black
        apply_theme(manim_scene=self, theme_name=theme)
        # You might want to set the default font and color for text here
        theme_preview_group = theme_preview()
        theme_preview_group.shift(m.DOWN * 0.5)

        theme_label = m.Text(
            "Catppuccin Latte Theme Preview",
            font="Courier New",
        )
        theme_label.to_corner(buff=0.5)

        self.add(theme_preview_group)
        self.add(theme_label)

        self.wait(0.2)

        self.remove(theme_preview_group)
        self.add(theme_label)





    def construct(self):
        my_theme = theme_preview()
        self.add(my_theme)


if __name__ == '__main__':
    import os
    from pathlib import Path

    FLAGS = "-pqm -s"
    SCENE = "CatppucinLattePreview"

    file_path = Path(__file__).resolve()
    os.system(f"manim {Path(__file__).resolve()} {SCENE} {FLAGS}")

