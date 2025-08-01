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
        # "Monokai Pro Light"
        theme = "Monokai Pro Light"
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True)

        theme_preview_group = theme_preview()
        theme_preview_group.shift(m.DOWN * 0.5)

        theme_label = m.Text(
            text=theme,
            font="Courier New",
        )
        theme_label.to_edge(m.UP, buff=0.5)

        self.add(theme_preview_group)
        self.add(theme_label)

        self.wait(0.2)





if __name__ == '__main__':
    import os
    from pathlib import Path

    FLAGS = "-pqh -s"
    SCENE = "ThemeGif"

    file_path = Path(__file__).resolve()
    os.system(f"manim {Path(__file__).resolve()} {SCENE} {FLAGS}")

