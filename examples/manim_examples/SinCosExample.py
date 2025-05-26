import manim as m
import numpy as np

from manim_themes.manim_theme import apply_theme


class AxesExample(m.Scene):

    def setup(self):
        # Set the background color to a light beige
        theme = "Ubuntu"
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True)
        m.Text.set_default(font="Courier New", color=m.GREEN)
        m.Tex.set_default(color=m.RED)
        m.MathTex.set_default(color=m.RED)

    def construct(self):
        axes = m.Axes(
            x_range=[-10, 10.3, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=10,
            axis_config={"color": m.GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(-10, 10.01, 2),
                "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
            },
            tips=False,
        )
        axes_labels = axes.get_axis_labels()
        sin_graph = axes.plot(lambda x: np.sin(x), color=m.BLUE)
        cos_graph = axes.plot(lambda x: np.cos(x), color=m.RED)

        sin_label = axes.get_graph_label(
            sin_graph, "\\sin(x)", x_val=-10, direction=m.UP / 2
        )
        cos_label = axes.get_graph_label(cos_graph, label="\\cos(x)")

        vert_line = axes.get_vertical_line(
            axes.i2gp(m.TAU, cos_graph), color=m.YELLOW, line_func=m.Line
        )
        line_label = axes.get_graph_label(
            cos_graph, r"x=2\pi", x_val=m.TAU, direction=m.UR, color=m.WHITE
        )

        plot = m.VGroup(axes, sin_graph, cos_graph, vert_line)
        labels = m.VGroup(axes_labels, sin_label, cos_label, line_label)
        self.add(plot, labels)


if __name__ == '__main__':
    import os
    from pathlib import Path

    FLAGS = "-pqm"
    SCENE = "AxesExample"

    file_path = Path(__file__).resolve()
    os.system(f"manim {Path(__file__).resolve()} {SCENE} {FLAGS}")

