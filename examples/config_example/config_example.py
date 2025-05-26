import manim as m

from manim_themes.manim_theme import apply_theme


class ThemeExample(m.Scene):

    def setup(self):
        # Set the background color to a light beige
        theme = "0x96f"
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True)
        m.Text.set_default(font="Courier New", color=m.GREEN)

    def construct(self):
        my_text = m.Text("Hello World")
        red_text = m.Text("I Use Ghostty BTW", color=m.RED)
        red_text.next_to(my_text, m.DOWN)

        text_group = m.VGroup(my_text, red_text).move_to(m.ORIGIN)

        self.play(m.FadeIn(text_group))


if __name__ == '__main__':
    import os
    from pathlib import Path

    FLAGS = "-pqm"
    SCENE = "ThemeExample"

    file_path = Path(__file__).resolve()
    os.system(f"manim {Path(__file__).resolve()} {SCENE} {FLAGS}")

