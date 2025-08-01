import manim as m

from manim_themes.manim_theme import apply_theme
from manim_themes.theme_preview import theme_preview


class ThemeGif(m.Scene):


    def construct(self):
        themes = [
            "Ghostty Default StyleDark",
            "Terminal Basic Dark",
            "The Hulk",
            "Tinacious Design (Dark)",
            "tokyonight-storm",
            "ToyChest",
            "Ubuntu",
            "UltraViolent",
            "UltraDark",
            "UnderTheSea",
            "Urple",
            "WildCherry",
            "wilmersdorf",
            "Wombat",
        ]
        theme = "Terminal Basic Dark"
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True)

        theme_preview_group = theme_preview()
        theme_preview_group.shift(m.DOWN * 0.5)

        theme_label = m.Text(
            text=theme,
            font="Courier New",
        )
        theme_label.to_edge(m.UP, buff=0.5)

        self.add(theme_label)

        ax = m.Axes(
            x_range=[0, 5],
            y_range=[0, 6],
            x_axis_config={"numbers_to_include": [2, 3]},
            tips=False,
        )

        labels = ax.get_axis_labels()

        curve_1 = ax.plot(lambda x: 4 * x - x ** 2, x_range=[0, 4], color=m.BLUE_C)
        curve_2 = ax.plot(
            lambda x: 0.8 * x ** 2 - 3 * x + 4,
            x_range=[0, 4],
            color=m.GREEN_B,
        )

        line_1 = ax.get_vertical_line(ax.input_to_graph_point(2, curve_1), color=m.YELLOW)
        line_2 = ax.get_vertical_line(ax.i2gp(3, curve_1), color=m.YELLOW)

        riemann_area = ax.get_riemann_rectangles(curve_1, x_range=[0.3, 0.6], dx=0.03, color=m.BLUE, fill_opacity=0.5)
        area = ax.get_area(curve_2, [2, 3], bounded_graph=curve_1, color=m.GREY, opacity=0.5)

        graph_group = m.VGroup(ax, labels, curve_1, curve_2, line_1, line_2, riemann_area, area)
        graph_group.scale(0.5)
        graph_group.to_edge(m.LEFT)

        theme_label = m.Text(
            text=theme,
            font="Courier New",
        )
        theme_label.to_edge(m.UP, buff=0.5)

        m0 = m.Dot()
        m1 = m.AnnotationDot()
        m2 = m.LabeledDot("ii")
        m3 = m.LabeledDot(m.MathTex(r"\alpha").set_color(m.ORANGE))
        m4 = m.CurvedArrow(2 * m.LEFT, 2 * m.RIGHT, radius=-5)
        m5 = m.CurvedArrow(2 * m.LEFT, 2 * m.RIGHT, radius=8)
        m6 = m.CurvedDoubleArrow(m.ORIGIN, 2 * m.RIGHT)

        m_group = m.VGroup(m0, m1, m2, m3, m4, m5, m6).arrange(m.DOWN, buff=0.2)

        m_group.next_to(graph_group, m.RIGHT)

        circle = m.Circle()
        square = m.Square()

        geo_group = m.VGroup(circle, square).arrange(m.DOWN, buff=0.2)
        geo_group.next_to(m_group, m.RIGHT)

        self.add(graph_group, theme_label, m_group, geo_group)

        self.wait(0.5)





if __name__ == '__main__':
    import os
    from pathlib import Path

    FLAGS = "-pqh -s"
    SCENE = "ThemeExample"

    file_path = Path(__file__).resolve()
    os.system(f"manim {Path(__file__).resolve()} {SCENE} {FLAGS}")

