import manim
from manim import *
import manim.utils.color.manim_colors as Colors

from manim_themes.manim_theme import apply_theme

def theme_preview() -> VGroup:
    def color_group(color):
        group = VGroup(
            *[
                Line(ORIGIN, RIGHT * 1.5, stroke_width=35, color=getattr(Colors, name.upper()))
                for name in subnames(color)
            ]
        ).arrange_submobjects(buff=0.4, direction=DOWN)

        name = Text(color).scale(0.6).next_to(group, UP, buff=0.3)
        if any(decender in color for decender in "gjpqy"):
            name.shift(DOWN * 0.08)
        group.add(name)
        return group

    def subnames(name):
        return [name + "_" + char for char in "abcde"]

    color_groups = VGroup(
        *[
            color_group(color)
            for color in [
                "blue",
                "teal",
                "green",
                "yellow",
                "gold",
                "red",
                "maroon",
                "purple",
            ]
        ]
    ).arrange_submobjects(buff=0.2, aligned_edge=DOWN)

    for line, char in zip(color_groups[0], "abcde"):
        color_groups.add(Text(char).scale(0.6).next_to(line, LEFT, buff=0.2))

    def named_lines_group(length, color_names, labels, align_to_block):
        colors = [getattr(Colors, color.upper()) for color in color_names]
        lines = VGroup(
            *[
                Line(
                    ORIGIN,
                    RIGHT * length,
                    stroke_width=55,
                    color=color,
                )
                for color in colors
            ]
        ).arrange_submobjects(buff=0.6, direction=DOWN)

        for line, name, color in zip(lines, labels, colors):
            line.add(Text(name, color=color.contrasting()).scale(0.6).move_to(line))
        lines.next_to(color_groups, DOWN, buff=0.5).align_to(
            color_groups[align_to_block], LEFT
        )
        return lines

    other_colors = (
        "pink",
        "light_pink",
        "orange",
        "light_brown",
        "dark_brown",
        "gray_brown",
    )

    other_lines = named_lines_group(
        3.2,
        other_colors,
        other_colors,
        0,
    )

    gray_lines = named_lines_group(
        6.6,
        ["white"] + subnames("gray") + ["black"],
        [
            "white",
            "lighter_gray / gray_a",
            "light_gray / gray_b",
            "gray / gray_c",
            "dark_gray / gray_d",
            "darker_gray / gray_e",
            "black",
        ],
        2,
    )

    pure_colors = (
        "pure_red",
        "pure_green",
        "pure_blue",
    )

    pure_lines = named_lines_group(
        3.2,
        pure_colors,
        pure_colors,
        6,
    )

    preview = manim.VGroup(color_groups, other_lines, gray_lines, pure_lines)
    preview.move_to(ORIGIN)
    return preview

if __name__ == '__main__':
    import os
    from pathlib import Path

    FLAGS = "-pqm -s"
    SCENE = "ColorsOverview"

    file_path = Path(__file__).resolve()
    os.system(f"manim {Path(__file__).resolve()} {SCENE} {FLAGS}")

