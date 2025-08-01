import os
import plistlib
import requests
import pathlib

import manim as m


from manim_themes.logger import log

def download_iterm2_theme(theme_name: str, themes_dir: str | pathlib.Path="./media/themes"):
    """
    Downloads the iTerm2 theme from GitHub and saves it to the specified directory.

    :param theme_name: the name of the theme to download (without the .itermcolors extension)
    :param themes_dir: the directory where the theme will be saved
    :return: None
    """
    os.makedirs(themes_dir, exist_ok=True)
    base_url = "https://raw.githubusercontent.com/mbadolato/iTerm2-Color-Schemes/refs/heads/master/schemes"
    theme_file = os.path.join(themes_dir, f"{theme_name}.itermcolors")
    url = f"{base_url}/{theme_name}.itermcolors"
    response = requests.get(url)
    if response.status_code == 200:
        with open(theme_file, "wb") as f:
            f.write(response.content)
    else:
        raise FileNotFoundError(f"Theme '{theme_name}' konnte nicht von GitHub geladen werden.")

def load_iterm2_theme(theme_name:str, themes_dir: str | pathlib.Path="./media/themes"):
    """
    Loads an iTerm2 theme (.itermcolors) as a Python dictionary.
    Downloads the theme automatically if it is not already present in the specified directory.

    :param theme_name: the name of the theme to load (without the .itermcolors extension)
    :param themes_dir: the directory where the theme is stored
    :return: a dictionary containing the iTerm2 theme colors
    """
    theme_file = os.path.join(themes_dir, f"{theme_name}.itermcolors")
    if not os.path.isfile(theme_file):
        download_iterm2_theme(theme_name, themes_dir)
    with open(theme_file, "rb") as f:
        theme_dict = plistlib.load(f)
    return theme_dict


def rgb_dict_to_hex(color_dict):
    r = int(round(color_dict['Red Component'] * 255))
    g = int(round(color_dict['Green Component'] * 255))
    b = int(round(color_dict['Blue Component'] * 255))
    return f"#{r:02X}{g:02X}{b:02X}"

def convert_colors_to_manim_colors(theme_dict):
    """
    Converts the iTerm2 theme colors to Manim colors.

    :param theme_dict: a dictionary containing the iTerm2 theme colors (values in range [0, 1])
    :return: a dictionary containing the Manim colors
    """
    return {k: m.ManimColor(rgb_dict_to_hex(v)) for k, v in theme_dict.items()}


def apply_theme(manim_scene: m.Scene, theme_name: str, themes_dir="./media/themes",
                skip_default_constructor_adjustment=False, **kwargs):
    """
    Applies the iTerm2 theme to a Manim scene.
    It basically overrides the manim default colors with the colors of the specified theme.
    The Scene object has to be passed to the function in order to change the background color.

    Available themes can be found here:
    https://iterm2colorschemes.com

    A theme contains the set of colors that are mapped to manim colors in the following way by default:


    Internally the module fetches the themes from Github:

    https://github.com/mbadolato/iTerm2-Color-Schemes/tree/master/schemes

    In case your have issues with the download, you please validate the URL and the theme name (especially the spelling of the theme).
    It has to match the name of the file in the Github repository.

    Example:

    The theme "Blazer" is stored in the Github repository as "Blazer.itermcolors".
    The corresponding file on Github is:

    https://github.com/mbadolato/iTerm2-Color-Schemes/blob/master/schemes/Blazer.itermcolors

    and the theme will be downloaded from:

    https://raw.githubusercontent.com/mbadolato/iTerm2-Color-Schemes/refs/heads/master/schemes/Blazer.itermcolors

    In order that everything works as expected the "Blazer" needs to be spelled with a capital "B".

    :param manim_scene:     The Manim scene to which the theme will be applied.
    :param theme_name:      A valid theme name from the iTerm2 themes repository.
    :param themes_dir:      The directory where the themes will be stored locally. Default is "./media/themes".
                            So you will find it alongside the other media files that manim creates.

    :param skip_default_constructor_adjustment: If set to True, the default constructor adjustments will not be applied.
                                                without adjustments text and other mobjects will use the manim default colors anyway.

    :return:                None
    """

    log.info(f"Applying theme '{theme_name}' to Scene '{manim_scene.__class__.__name__}'")

    theme = load_iterm2_theme(theme_name=theme_name, themes_dir=themes_dir)
    # convert the theme colors to hex
    theme_manim_colors = convert_colors_to_manim_colors(theme)

    # override colors


    m.WHITE = theme_manim_colors['Ansi 7 Color']
    m.BLACK = theme_manim_colors['Ansi 0 Color']

    m.GRAY_A = theme_manim_colors['Ansi 8 Color'].lighter(0.2)
    m.GREY_A = theme_manim_colors['Ansi 8 Color'].lighter(0.2)
    m.GRAY_B = theme_manim_colors['Ansi 8 Color'].lighter(0.1)
    m.GREY_B = theme_manim_colors['Ansi 8 Color'].lighter(0.1)
    m.GRAY_C = theme_manim_colors['Ansi 8 Color']
    m.GREY_C = theme_manim_colors['Ansi 8 Color']
    m.GRAY_D = theme_manim_colors['Ansi 8 Color'].darker(0.1)
    m.GREY_D = theme_manim_colors['Ansi 8 Color'].darker(0.1)
    m.GRAY_E = theme_manim_colors['Ansi 8 Color'].darker(0.2)
    m.GREY_E = theme_manim_colors['Ansi 8 Color'].darker(0.2)

    m.LIGHTER_GRAY = m.GRAY_A
    m.LIGHTER_GREY = m.GREY_A
    m.LIGHT_GRAY = m.GRAY_B
    m.LIGHT_GREY = m.GRAY_B
    
    m.GRAY = theme_manim_colors['Ansi 8 Color']
    m.GREY = theme_manim_colors['Ansi 8 Color']
    
    m.DARK_GRAY = m.GRAY_D
    m.DARK_GREY = m.GREY_D
    m.DARKER_GRAY = m.GRAY_E
    m.DARKER_GREY = m.GREY_E

    m.BLUE_A = theme_manim_colors['Ansi 4 Color'].lighter(0.2)
    m.BLUE_B = theme_manim_colors['Ansi 4 Color'].lighter(0.1)
    m.BLUE_C = theme_manim_colors['Ansi 4 Color']
    m.BLUE_D = theme_manim_colors['Ansi 4 Color'].darker(0.1)
    m.BLUE_E = theme_manim_colors['Ansi 4 Color'].darker(0.2)
    m.BLUE = theme_manim_colors['Ansi 4 Color']
    # m.PURE_BLUE = m.ManimColor("#0000FF")
    m.DARK_BLUE = theme_manim_colors['Ansi 4 Color'].darker(0.2)

    m.TEAL_A = theme_manim_colors['Ansi 6 Color'].lighter(0.2)
    m.TEAL_B = theme_manim_colors['Ansi 6 Color'].lighter(0.1)
    m.TEAL_C = theme_manim_colors['Ansi 6 Color']
    m.TEAL_D = theme_manim_colors['Ansi 6 Color'].darker(0.1)
    m.TEAL_E = theme_manim_colors['Ansi 6 Color'].darker(0.2)
    m.TEAL = theme_manim_colors['Ansi 6 Color']


    m.GREEN_A = theme_manim_colors['Ansi 2 Color'].lighter(0.2)
    m.GREEN_B = theme_manim_colors['Ansi 2 Color'].lighter(0.1)
    m.GREEN_C = theme_manim_colors['Ansi 2 Color']
    m.GREEN_D = theme_manim_colors['Ansi 2 Color'].darker(0.1)
    m.GREEN_E = theme_manim_colors['Ansi 2 Color'].darker(0.2)
    # PURE_GREEN = ManimColor("#00FF00")
    m.GREEN = theme_manim_colors['Ansi 2 Color']


    m.YELLOW_A = theme_manim_colors['Ansi 3 Color'].lighter(0.2)
    m.YELLOW_B = theme_manim_colors['Ansi 3 Color'].lighter(0.1)
    m.YELLOW_C = theme_manim_colors['Ansi 3 Color']
    m.YELLOW_D = theme_manim_colors['Ansi 3 Color'].darker(0.1)
    m.YELLOW_E = theme_manim_colors['Ansi 3 Color'].darker(0.2)
    m.YELLOW = theme_manim_colors['Ansi 3 Color']

    m.GOLD_A = theme_manim_colors['Ansi 11 Color'].lighter(0.2)
    m.GOLD_B = theme_manim_colors['Ansi 11 Color'].lighter(0.1)
    m.GOLD_C = theme_manim_colors['Ansi 11 Color']
    m.GOLD_D = theme_manim_colors['Ansi 11 Color'].darker(0.1)
    m.GOLD_E = theme_manim_colors['Ansi 11 Color'].darker(0.2)
    m.GOLD = theme_manim_colors['Ansi 11 Color']

    m.RED_A = theme_manim_colors['Ansi 1 Color'].lighter(0.2)
    m.RED_B = theme_manim_colors['Ansi 1 Color'].lighter(0.1)
    m.RED_C = theme_manim_colors['Ansi 1 Color']
    m.RED_D = theme_manim_colors['Ansi 1 Color'].darker(0.1)
    m.RED_E = theme_manim_colors['Ansi 1 Color'].darker(0.2)
    # m.PURE_RED = ManimColor("#FF0000")
    m.RED = theme_manim_colors['Ansi 1 Color']


    m.MAROON_A = theme_manim_colors['Ansi 9 Color'].lighter(0.2)
    m.MAROON_B = theme_manim_colors['Ansi 9 Color'].lighter(0.1)
    m.MAROON_C = theme_manim_colors['Ansi 9 Color']
    m.MAROON_D = theme_manim_colors['Ansi 9 Color'].darker(0.1)
    m.MAROON_E = theme_manim_colors['Ansi 9 Color'].darker(0.2)
    m.MAROON = theme_manim_colors['Ansi 9 Color']

    m.PURPLE_A = theme_manim_colors['Ansi 5 Color'].lighter(0.2)
    m.PURPLE_B = theme_manim_colors['Ansi 5 Color'].lighter(0.1)
    m.PURPLE_C = theme_manim_colors['Ansi 5 Color']
    m.PURPLE_D = theme_manim_colors['Ansi 5 Color'].darker(0.1)
    m.PURPLE_E = theme_manim_colors['Ansi 5 Color'].darker(0.2)
    m.PURPLE = theme_manim_colors['Ansi 5 Color']


    m.PINK =  theme_manim_colors['Ansi 5 Color']
    m.LIGHT_PINK =  theme_manim_colors['Ansi 13 Color']

    m.ORANGE = 0.5 * m.RED + 0.5 * m.YELLOW
    m.LIGHT_BROWN = m.ORANGE.lighter(0.1)
    m.DARK_BROWN = m.ORANGE.darker(0.1)

    m.GRAY_BROWN = 0.5 * m.LIGHT_BROWN + 0.5 * m.GRAY
    m.GREY_BROWN = 0.5 * m.LIGHT_BROWN + 0.5 * m.GREY

    # Colors used for Manim Community's logo and banner

    # LOGO_WHITE = ManimColor("#ECE7E2")
    # LOGO_GREEN = ManimColor("#87C2A5")
    # LOGO_BLUE = ManimColor("#525893")
    # LOGO_RED = ManimColor("#E07A5F")
    # LOGO_BLACK = ManimColor("#343434")

    # set background color
    manim_scene.camera.background_color = theme_manim_colors['Background Color']

    if skip_default_constructor_adjustment:
        # just break here if you want to skip the default constructor adjustments
        return

    m.Text.set_default(
        # font="Courier New",
        color=m.WHITE
    )
    m.Tex.set_default(color=m.WHITE)
    m.MathTex.set_default(color=m.WHITE)

    # Mobjects
    m.Mobject.set_default(color=m.WHITE)
    m.VMobject.set_default(color=m.WHITE)

    m.Rectangle.set_default(color=m.WHITE)
    m.AnnotationDot.set_default(stroke_color=m.WHITE, fill_color=m.BLUE)
    m.Arc.set_default(stroke_color=m.WHITE)
    m.AnnularSector.set_default(color=m.WHITE)

    m.Angle.set_default(color=m.WHITE)
    m.AnnotationDot.set_default(stroke_color=m.WHITE)
    m.Annulus.set_default(color=m.WHITE)
    m.Arrow.set_default(color=m.WHITE)
    m.Arrow3D.set_default(color=m.WHITE)
    m.ArrowVectorField.set_default(color=m.WHITE)
    m.Code.set_default(
        font="Courier New",
        color=m.WHITE
    )
    m.CubicBezier.set_default(color=m.WHITE)
    m.DashedVMobject.set_default(color=m.WHITE)
    m.Dot.set_default(color=m.WHITE)
    m.Dot3D.set_default(color=m.WHITE)
    m.Line.set_default(color=m.WHITE)
    m.Line3D.set_default(color=m.WHITE)
    m.MarkupText.set_default(color=m.WHITE)
    m.Polygon.set_default(color=m.WHITE)
    m.Rectangle.set_default(color=m.WHITE)
    m.SingleStringMathTex.set_default(color=m.WHITE)
    m.StreamLines.set_default(color=m.WHITE)
    m.TracedPath.set_default(stroke_color=m.WHITE)
    m.VectorField.set_default(color=m.WHITE)

    m.NumberPlane().set_default(
        background_line_style={
            "stroke_color": m.GRAY,
        },
        x_axis_config={"stroke_color": m.WHITE},
        y_axis_config={"stroke_color": m.WHITE},
    )

    m.Table.set_default(line_config={"color": m.WHITE})






