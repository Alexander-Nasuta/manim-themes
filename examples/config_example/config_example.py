import manim as m

from manim_themes.manim_theme import apply_theme


class ConfigExample(m.Scene):

    def setup(self):
        # Set the background color to a light beige
        theme = "Andromeda"
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True)

        # Here are the configs tht manim-themes sets by default
        # feel free to change them to your liking
        m.Text.set_default(
            color=m.WHITE
        )
        m.Tex.set_default(color=m.WHITE)
        m.MathTex.set_default(color=m.WHITE)

        # Mobjects
        m.Mobject.set_default(color=m.WHITE)
        m.VMobject.set_default(color=m.WHITE)

        m.Rectangle.set_default(color=m.RED)
        m.AnnotationDot.set_default(stroke_color=m.WHITE, fill_color=m.BLUE)
        m.Arc.set_default(stroke_color=m.WHITE)
        m.AnnularSector.set_default(color=m.WHITE)

        m.NumberPlane().set_default(
            background_line_style={
                "stroke_color": m.GRAY,
            },
            x_axis_config={"stroke_color": m.WHITE},
            y_axis_config={"stroke_color": m.WHITE},
        )
        m.Arrow.set_default(color=m.WHITE)
        m.Dot.set_default(color=m.WHITE)

    def construct(self):
        my_text = m.Text("Hello World")
        green_text = m.Text("I Use Neovim BTW", color=m.GREEN)
        green_text.next_to(my_text, m.DOWN)

        text_group = m.VGroup(my_text, green_text).move_to(m.ORIGIN)

        self.play(m.FadeIn(text_group))


if __name__ == '__main__':
    import os
    from pathlib import Path

    FLAGS = "-pqm"
    SCENE = "ConfigExample"

    file_path = Path(__file__).resolve()
    os.system(f"manim {Path(__file__).resolve()} {SCENE} {FLAGS}")

