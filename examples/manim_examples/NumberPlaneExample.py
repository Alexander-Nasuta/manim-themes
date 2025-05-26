import manim as m


from manim_themes.manim_theme import apply_theme

class NumberPlaneExample(m.Scene):

    def setup(self):
        # Set the background color to a light beige
        theme = "Obsidian"
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True)



    def construct(self):
        dot = m.Dot(m.ORIGIN)
        arrow = m.Arrow(m.ORIGIN, [2, 2, 0], buff=0)


        numberplane = m.NumberPlane()
        origin_text = m.Text('(0, 0)').next_to(dot, m.DOWN)
        tip_text = m.Text('(2, 2)').next_to(arrow.get_end(), m.RIGHT)
        self.add(numberplane, dot, arrow, origin_text, tip_text)


if __name__ == '__main__':
    import os
    from pathlib import Path

    FLAGS = "-pqm"
    SCENE = "AxesExample"

    file_path = Path(__file__).resolve()
    os.system(f"manim {Path(__file__).resolve()} {SCENE} {FLAGS}")

