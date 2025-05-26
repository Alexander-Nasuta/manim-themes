# Example Gallery

This gallery contains a collection of code snippets together with their corresponding output, illustrating different colors themes in Manim and example objects.


```{eval-rst}
.. manim:: NumberPlaneExample
    :save_last_frame:
    
    
    import manim as m

    from manim_themes.manim_theme import apply_theme
    
    class NumberPlaneExample(m.Scene):
    
        def setup(self):
            # Set the background color to a light beige
            theme = "Obsidian"
            apply_theme(manim_scene=self, theme_name=theme)
    
    
    
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


```


```{eval-rst}
.. manim:: PolygonExample
    
    
    import manim as m
    import numpy as np
    
    from manim_themes.manim_theme import apply_theme
    
    class PolygonExample(m.Scene):
    
        def setup(self):
            # Set the background color to a light beige
            #theme = "Retro"
            theme="CrayonPonyFish"
            apply_theme(manim_scene=self, theme_name=theme)
    
    
    
        def get_rectangle_corners(self, bottom_left, top_right):
            return [
                (top_right[0], top_right[1]),
                (bottom_left[0], top_right[1]),
                (bottom_left[0], bottom_left[1]),
                (top_right[0], bottom_left[1]),
            ]
    
        def construct(self):
            ax = m.Axes(
                x_range=[0, 10],
                y_range=[0, 10],
                x_length=6,
                y_length=6,
                axis_config={"include_tip": False},
            )
    
            t = m.ValueTracker(5)
            k = 25
    
            graph = ax.plot(
                lambda x: k / x,
                color=m.YELLOW_D,
                x_range=[k / 10, 10.0, 0.01],
                use_smoothing=False,
            )
    
            def get_rectangle():
                polygon = m.Polygon(
                    *[
                        ax.c2p(*i)
                        for i in self.get_rectangle_corners(
                            (0, 0), (t.get_value(), k / t.get_value())
                        )
                    ]
                )
                polygon.stroke_width = 1
                polygon.set_fill(m.BLUE, opacity=0.5)
                polygon.set_stroke(m.YELLOW_B)
                return polygon
    
            polygon = m.always_redraw(get_rectangle)
    
            dot = m.Dot()
            dot.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), k / t.get_value())))
            dot.set_z_index(10)
    
            self.add(ax, graph, dot)
            self.play(m.Create(polygon))
            self.play(t.animate.set_value(10))
            self.play(t.animate.set_value(k / 10))
            self.play(t.animate.set_value(5))
    
    
    if __name__ == '__main__':
        import os
        from pathlib import Path
    
        FLAGS = "-pqm"
        SCENE = "PolygonExample"
    
        file_path = Path(__file__).resolve()
        os.system(f"manim {Path(__file__).resolve()} {SCENE} {FLAGS}")
    

```


```{eval-rst}
.. manim:: AxesExample
    :save_last_frame:
    
    
    import manim as m
    import numpy as np
    
    from manim_themes.manim_theme import apply_theme
    
    
    class AxesExample(m.Scene):
    
        def setup(self):
            # Set the background color to a light beige
            theme = "Ubuntu"
            apply_theme(manim_scene=self, theme_name=theme)
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
    

```



```{eval-rst}
.. manim:: TableExample
    :save_last_frame:
    
    
    import manim as m
    import numpy as np
    
    from manim_themes.manim_theme import apply_theme
    
    class TableExample(m.Scene):
    
        def setup(self):
            # Set the background color to a light beige
            #theme = "Retro"
            theme="Obsidian"
            apply_theme(manim_scene=self, theme_name=theme)
    
            m.Text.set_default(
                font="Courier New",
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
                    "stroke_color": m.RED,
                },
                x_axis_config={"stroke_color": m.GREEN},
                y_axis_config={"stroke_color": m.BLUE},
            )
            m.Arrow.set_default(color=m.GOLD)
            m.Dot.set_default(color=m.PURPLE)
    
    
        def construct(self):
            t0 = m.Table(
                [["First", "Second"],
                 ["Third", "Fourth"]],
                row_labels=[m.Text("R1"), m.Text("R2")],
                col_labels=[m.Text("C1"), m.Text("C2")],
                top_left_entry=m.Text("TOP"))
            t0.add_highlighted_cell((2, 2), color=m.GREEN)
            x_vals = np.linspace(-2, 2, 5)
            y_vals = np.exp(x_vals)
            t1 = m.DecimalTable(
                [x_vals, y_vals],
                row_labels=[m.MathTex("x"), m.MathTex("f(x)")],
                include_outer_lines=True)
            t1.add(t1.get_cell((2, 2), color=m.RED))
            t2 = m.MathTable(
                [["+", 0, 5, 10],
                 [0, 0, 5, 10],
                 [2, 2, 7, 12],
                 [4, 4, 9, 14]],
                include_outer_lines=True)
            t2.get_horizontal_lines()[:3].set_color(m.BLUE)
            t2.get_vertical_lines()[:3].set_color(m.BLUE)
            t2.get_horizontal_lines()[:3].set_z_index(1)
            cross = m.VGroup(
                m.Line(m.UP + m.LEFT, m.DOWN + m.RIGHT),
                m.Line(m.UP + m.RIGHT, m.DOWN + m.LEFT))
            a = m.Circle().set_color(m.RED).scale(0.5)
            b = cross.set_color(m.BLUE).scale(0.5)
            t3 = m.MobjectTable(
                [[a.copy(), b.copy(), a.copy()],
                 [b.copy(), a.copy(), a.copy()],
                 [a.copy(), b.copy(), b.copy()]])
            t3.add(m.Line(
                t3.get_corner(m.DL), t3.get_corner(m.UR)
            ).set_color(m.RED))
            vals = np.arange(1, 21).reshape(5, 4)
            t4 = m.IntegerTable(
                vals,
                include_outer_lines=True
            )
            g1 = m.Group(t0, t1).scale(0.5).arrange(buff=1).to_edge(m.UP, buff=1)
            g2 = m.Group(t2, t3, t4).scale(0.5).arrange(buff=1).to_edge(m.DOWN, buff=1)
            self.add(g1, g2)
    
    
    if __name__ == '__main__':
        import os
        from pathlib import Path
    
        FLAGS = "-pqm -s"
        SCENE = "TableExample"
    
        file_path = Path(__file__).resolve()
        os.system(f"manim {Path(__file__).resolve()} {SCENE} {FLAGS}")
    

```


```{eval-rst}
.. manim:: ThemeCarouselObjects
    
    
    import manim as m
    import random
    
    from manim_themes.manim_theme import apply_theme
    from manim_themes.theme_preview import theme_preview
    
    
    class ThemeCarouselObjects(m.Scene):
    
    
        def construct(self):
            themes = [
                "0x96f",
                "3024 Day",
                "3024 Night",
                "BlueDolphin",
                "CGA",
                "CutiePro",
                "DjangoRebornAgain",
                "DjangoSmooth",
                "Ghostty Default StyleDark",
                "NvimDark",
                "NvimLight",
                "PaleNightHC",
                "RetroLegends",
                "shades-of-purple",
                "SleepyHollow",
                "Aardvark Blue",
                "Abernathy",
                "Adventure",
                "AdventureTime",
                "Adwaita",
                "Adwaita Dark",
                "Afterglow",
                "Alabaster",
                "AlienBlood",
                "Andromeda",
                "Apple System Colors",
                "Apple System Colors Light",
                "arcoiris",
                "Ardoise",
                "Argonaut",
                "Arthur",
                "AtelierSulphurpool",
                "Atom",
                "AtomOneDark",
                "FrontEndDelight",
                "Aura",
                "Aurora",
                "ayu",
                "ayu_light",
                "Ayu Mirage",
                "Banana Blueberry",
                "Batman",
                "Belafonte Day",
                "Belafonte Night",
                "BirdsOfParadise",
                "Blazer",
                "Blue Matrix",
                "BlueBerryPie",
                "BlulocoDark",
                "BlulocoLight",
                "Borland",
                "Breeze",
                "Bright Lights",
                "Broadcast",
                "Brogrammer",
                "C64",
                "Calamity",
                "catppuccin-frappe",
                "catppuccin-latte",
                "catppuccin-macchiato",
                "catppuccin-mocha",
                "ENCOM",
                "Chalk",
                "Chalkboard",
                "ChallengerDeep",
                "Chester",
                "Ciapre",
                "citruszest",
                "CLRS",
                "Cobalt2",
                "Cobalt Neon",
                "CobaltNext",
                "CobaltNext-Dark",
                "CobaltNext-Minimal",
                "CrayonPonyFish",
                "Cyberdyne",
                "cyberpunk",
                "CyberpunkScarletProtocol",
                "Dark Modern",
                "Dark Pastel",
                "Dark+",
                "darkermatrix",
                "darkmatrix",
                "Darkside",
                "dayfox",
                "deep",
                "Desert",
                "detuned",
                "Dimidium",
                "DimmedMonokai",
                "Django",
                "DoomOne",
                "Doom Peacock",
                "DotGov",
                "Dracula",
                "Dracula+",
                "duckbones",
                "Duotone Dark",
                "Earthsong",
                "electron-highlighter",
                "Elegant",
                "Elemental",
                "Elementary",
                "Embark",
                "embers-dark",
                "terafox",
                "Espresso",
                "Espresso Libre",
                "Everblush",
                "Everforest Dark - Hard",
                "Fahrenheit",
                "Fairyfloss",
                "farmhouse-dark",
                "farmhouse-light",
                "Fideloper",
                "Firefly Traditional",
                "Firewatch",
                "FishTank",
                "Flat",
                "Flatland",
                "flexoki-dark",
                "flexoki-light",
                "Floraverse",
                "FirefoxDev",
                "Framer",
                "FunForrest",
                "Galaxy",
                "Galizur",
                "GitLab-Dark",
                "GitLab-Dark-Grey",
                "GitLab-Light",
                "Github",
                "GitHub-Dark-Colorblind",
                "GitHub-Dark-Default",
                "GitHub-Dark-Dimmed",
                "GitHub-Dark-High-Contrast",
                "GitHub-Light-Colorblind",
                "GitHub-Light-Default",
                "GitHub-Light-High-Contrast",
                "GitHub Dark",
                "Glacier",
                "Grape",
                "Grass",
                "Grey-green",
                "gruber-darker",
                "GruvboxDark",
                "GruvboxDarkHard",
                "GruvboxLight",
                "GruvboxLightHard",
                "gruvbox-material",
                "Guezwhoz",
                "Hacktober",
                "Hardcore",
                "Harper",
                "Havn Daggry",
                "Havn Skumring",
                "ForestBlue",
                "HaX0R_GR33N",
                "HaX0R_R3D",
                "heeler",
                "Highway",
                "Hipster Green",
                "Hivacruz",
                "Homebrew",
                "Hopscotch",
                "Hopscotch.256",
                "Horizon",
                "Horizon-Bright",
                "Hurtado",
                "Hybrid",
                "IC_Green_PPL",
                "IC_Orange_PPL",
                "iceberg-dark",
                "iceberg-light",
                "idea",
                "idleToes",
                "IR_Black",
                "IRIX Console",
                "IRIX Terminal",
                "iTerm2 Dark Background",
                "iTerm2 Default",
                "iTerm2 Light Background",
                "iTerm2 Pastel Dark Background",
                "iTerm2 Smoooooth",
                "iTerm2 Solarized Dark",
                "iTerm2 Solarized Light",
                "iTerm2 Tango Dark",
                "iTerm2 Tango Light",
                "Jackie Brown",
                "Japanesque",
                "Jellybeans",
                "JetBrains Darcula",
                "jubi",
                "Kanagawa Dragon",
                "Kanagawa Wave",
                "kanagawabones",
                "Kibble",
                "Kolorit",
                "Konsolas",
                "kurokula",
                "Lab Fox",
                "Laser",
                "Later This Evening",
                "Lavandula",
                "LiquidCarbon",
                "LiquidCarbonTransparent",
                "LiquidCarbonTransparentInverse",
                "lovelace",
                "Man Page",
                "Mariana",
                "Material",
                "MaterialDark",
                "MaterialDarker",
                "MaterialDesignColors",
                "MaterialOcean",
                "Mathias",
                "matrix",
                "Medallion",
                "Melange_dark",
                "Melange_light",
                "Mellifluous",
                "mellow",
                "miasma",
                "midnight-in-mojave",
                "Mirage",
                "Misterioso",
                "Molokai",
                "MonaLisa",
                "Apple Classic",
                "sonokai",
                "nord-light",
                "Monokai Classic",
                "Monokai Pro",
                "Monokai Pro Light",
                "Monokai Pro Light Sun",
                "Monokai Pro Machine",
                "Monokai Pro Octagon",
                "Monokai Pro Ristretto",
                "Monokai Pro Spectrum",
                "Monokai Remastered",
                "Monokai Soda",
                "Monokai Vivid",
                "N0tch2k",
                "neobones_dark",
                "neobones_light",
                "Neon",
                "Neopolitan",
                "Neutron",
                "Night Owlish Light",
                "nightfox",
                "NightLion v1",
                "NightLion v2",
                "niji",
                "Nocturnal Winter",
                "nord",
                "nord-wave",
                "xcodelighthc",
                "Novel",
                "Obsidian",
                "Ocean",
                "OceanicMaterial",
                "Oceanic-Next",
                "Ollie",
                "OneHalfDark",
                "OneHalfLight",
                "Operator Mono Dark",
                "Overnight Slumber",
                "Oxocarbon",
                "Pandora",
                "Paraiso Dark",
                "PaulMillr",
                "PencilDark",
                "PencilLight",
                "Peppermint",
                "Piatto Light",
                "Pnevma",
                "Popping and Locking",
                "primary",
                "Pro",
                "Pro Light",
                "Purple Rain",
                "purplepeter",
                "Rapture",
                "Raycast_Dark",
                "Raycast_Light",
                "rebecca",
                "Red Alert",
                "Red Planet",
                "Red Sands",
                "Relaxed",
                "Retro",
                "Rippedcasts",
                "rose-pine",
                "rose-pine-dawn",
                "rose-pine-moon",
                "Rouge 2",
                "Royal",
                "Ryuuko",
                "Sakura",
                "Scarlet Protocol",
                "SeaShells",
                "Seafoam Pastel",
                "seoulbones_dark",
                "seoulbones_light",
                "Seti",
                "Shaman",
                "Slate",
                "Smyck",
                "Snazzy",
                "Snazzy Soft",
                "SoftServer",
                "solarized-osaka-night",
                "Solarized Darcula",
                "Solarized Dark Higher Contrast",
                "Solarized Dark - Patched",
                "SpaceGray",
                "Spacedust",
                "SpaceGray Bright",
                "SpaceGray Eighties",
                "SpaceGray Eighties Dull",
                "Spiderman",
                "Spring",
                "Square",
                "Squirrelsong Dark",
                "srcery",
                "starlight",
                "Sublette",
                "Subliminal",
                "Sugarplum",
                "Sundried",
                "Symfonic",
                "synthwave",
                "synthwave-everything",
                "SynthwaveAlpha",
                "Tango Adapted",
                "Tango Half Adapted",
                "Teerb",
                "Terminal Basic",
                "Terminal Basic Dark",
                "Thayer Bright",
                "The Hulk",
                "Tinacious Design (Dark)",
                "Tinacious Design (Light)",
                "tokyonight",
                "tokyonight-day",
                "tokyonight_moon",
                "tokyonight_night",
                "tokyonight-storm",
                "Tomorrow",
                "Tomorrow Night",
                "Tomorrow Night Blue",
                "Tomorrow Night Bright",
                "Tomorrow Night Burns",
                "Tomorrow Night Eighties",
                "ToyChest",
                "Treehouse",
                "Twilight",
                "Ubuntu",
                "UltraViolent",
                "UltraDark",
                "UnderTheSea",
                "Unikitty",
                "Urple",
                "Vaughn",
                "Vesper",
                "VibrantInk",
                "vimbones",
                "Violet Dark",
                "Violet Light",
                "WarmNeon",
                "Wez",
                "Whimsy",
                "WildCherry",
                "wilmersdorf",
                "Wombat",
                "Wryan",
                "xcodedark",
                "xcodedarkhc",
                "xcodelight",
                "AtomOneLight",
                "xcodewwdc",
                "zenbones",
                "zenbones_dark",
                "zenbones_light",
                "Zenburn",
                "zenburned",
                "zenwritten_dark",
                "zenwritten_light",
            ]
            random.shuffle(themes)
            # get a random sample of 20 themes from the list
            # every time the docs are built, a different set of themes is shown :)
            for theme in themes[:20]:
                apply_theme(manim_scene=self, theme_name=theme, light_theme=True)
    
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
    
                self.remove(graph_group, theme_label, m_group, geo_group)
    
    if __name__ == '__main__':
        import os
        from pathlib import Path
    
        FLAGS = "-pqm"
        SCENE = "ThemeCarouselObjects"
    
        file_path = Path(__file__).resolve()
        os.system(f"manim {Path(__file__).resolve()} {SCENE} {FLAGS}")
    

```

