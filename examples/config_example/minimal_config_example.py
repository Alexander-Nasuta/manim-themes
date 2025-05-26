import manim as m

from manim_themes.manim_theme import apply_theme


class MinimalThemeExample(m.Scene):

    def setup(self):
        # Set the background color to a light beige
        theme = "Andromeda"
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True)

    def construct(self):
        my_text = m.Text("Hello World")
        maroon_text = m.Text("I use Manim BTW", color=m.MAROON)
        maroon_text.next_to(my_text, m.DOWN)

        text_group = m.VGroup(my_text, maroon_text).move_to(m.ORIGIN)

        self.play(m.FadeIn(text_group))


if __name__ == '__main__':
    import os
    from pathlib import Path

    FLAGS = "-pqm -s"
    SCENE = "MinimalThemeExample"

    file_path = Path(__file__).resolve()
    os.system(f"manim {Path(__file__).resolve()} {SCENE} {FLAGS}")

