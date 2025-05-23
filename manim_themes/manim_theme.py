import os
import plistlib
import requests

import manim
from manim import *

from manim_themes.logger import log

def download_iterm2_theme(theme_name, themes_dir="./media/themes"):
    """
    Lädt das Theme von GitHub herunter, falls es nicht lokal vorhanden ist.
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

def load_iterm2_theme(theme_name, themes_dir="./media/themes"):
    """
    Lädt ein iTerm2-Theme (.itermcolors) als Python-Dict.
    Lädt das Theme ggf. automatisch herunter.
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


    :param theme_dict:
    :return:
    """
    return {k: manim.ManimColor(rgb_dict_to_hex(v)) for k, v in theme_dict.items()}


def apply_theme(manim_scene: manim.Scene, theme_name: str, themes_dir="./media/themes", light_theme=False):
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
    :return:                None
    """

    log.info(f"Applying theme '{theme_name}' to Scene '{manim_scene.__class__.__name__}'")

    theme = load_iterm2_theme(theme_name=theme_name, themes_dir=themes_dir)
    # convert the theme colors to hex
    theme_manim_colors = convert_colors_to_manim_colors(theme)

    # override colors


    manim.WHITE = theme_manim_colors['Ansi 7 Color']
    manim.BLACK = theme_manim_colors['Ansi 0 Color']

    manim.GRAY_A = theme_manim_colors['Ansi 8 Color'].lighter(0.2)
    manim.GREY_A = theme_manim_colors['Ansi 8 Color'].lighter(0.2)
    manim.GRAY_B = theme_manim_colors['Ansi 8 Color'].lighter(0.1)
    manim.GREY_B = theme_manim_colors['Ansi 8 Color'].lighter(0.1)
    manim.GRAY_C = theme_manim_colors['Ansi 8 Color']
    manim.GREY_C = theme_manim_colors['Ansi 8 Color']
    manim.GRAY_D = theme_manim_colors['Ansi 8 Color'].darker(0.1)
    manim.GREY_D = theme_manim_colors['Ansi 8 Color'].darker(0.1)
    manim.GRAY_E = theme_manim_colors['Ansi 8 Color'].darker(0.2)
    manim.GREY_E = theme_manim_colors['Ansi 8 Color'].darker(0.2)

    manim.LIGHTER_GRAY = manim.GRAY_A
    manim.LIGHTER_GREY = manim.GREY_A
    manim.LIGHT_GRAY = manim.GRAY_B
    manim.LIGHT_GREY = manim.GRAY_B
    
    manim.GRAY = theme_manim_colors['Ansi 8 Color']
    manim.GREY = theme_manim_colors['Ansi 8 Color']
    
    manim.DARK_GRAY = manim.GRAY_D
    manim.DARK_GREY = manim.GREY_D
    manim.DARKER_GRAY = manim.GRAY_E
    manim.DARKER_GREY = manim.GREY_E

    manim.BLUE_A = theme_manim_colors['Ansi 4 Color'].lighter(0.2)
    manim.BLUE_B = theme_manim_colors['Ansi 4 Color'].lighter(0.1)
    manim.BLUE_C = theme_manim_colors['Ansi 4 Color']
    manim.BLUE_D = theme_manim_colors['Ansi 4 Color'].darker(0.1)
    manim.BLUE_E = theme_manim_colors['Ansi 4 Color'].darker(0.2)
    manim.BLUE = theme_manim_colors['Ansi 4 Color']
    # manim.PURE_BLUE = manim.ManimColor("#0000FF")
    manim.DARK_BLUE = theme_manim_colors['Ansi 4 Color'].darker(0.2)

    manim.TEAL_A = theme_manim_colors['Ansi 6 Color'].lighter(0.2)
    manim.TEAL_B = theme_manim_colors['Ansi 6 Color'].lighter(0.1)
    manim.TEAL_C = theme_manim_colors['Ansi 6 Color']
    manim.TEAL_D = theme_manim_colors['Ansi 6 Color'].darker(0.1)
    manim.TEAL_E = theme_manim_colors['Ansi 6 Color'].darker(0.2)
    manim.TEAL = theme_manim_colors['Ansi 6 Color']


    manim.GREEN_A = theme_manim_colors['Ansi 2 Color'].lighter(0.2)
    manim.GREEN_B = theme_manim_colors['Ansi 2 Color'].lighter(0.1)
    manim.GREEN_C = theme_manim_colors['Ansi 2 Color']
    manim.GREEN_D = theme_manim_colors['Ansi 2 Color'].darker(0.1)
    manim.GREEN_E = theme_manim_colors['Ansi 2 Color'].darker(0.2)
    # PURE_GREEN = ManimColor("#00FF00")
    manim.GREEN = theme_manim_colors['Ansi 2 Color']


    manim.YELLOW_A = theme_manim_colors['Ansi 3 Color'].lighter(0.2)
    manim.YELLOW_B = theme_manim_colors['Ansi 3 Color'].lighter(0.1)
    manim.YELLOW_C = theme_manim_colors['Ansi 3 Color']
    manim.YELLOW_D = theme_manim_colors['Ansi 3 Color'].darker(0.1)
    manim.YELLOW_E = theme_manim_colors['Ansi 3 Color'].darker(0.2)
    manim.YELLOW = theme_manim_colors['Ansi 3 Color']

    manim.GOLD_A = theme_manim_colors['Ansi 11 Color'].lighter(0.2)
    manim.GOLD_B = theme_manim_colors['Ansi 11 Color'].lighter(0.1)
    manim.GOLD_C = theme_manim_colors['Ansi 11 Color']
    manim.GOLD_D = theme_manim_colors['Ansi 11 Color'].darker(0.1)
    manim.GOLD_E = theme_manim_colors['Ansi 11 Color'].darker(0.2)
    manim.GOLD = theme_manim_colors['Ansi 11 Color']

    manim.RED_A = theme_manim_colors['Ansi 4 Color'].lighter(0.2)
    manim.RED_B = theme_manim_colors['Ansi 4 Color'].lighter(0.1)
    manim.RED_C = theme_manim_colors['Ansi 4 Color']
    manim.RED_D = theme_manim_colors['Ansi 4 Color'].darker(0.1)
    manim.RED_E = theme_manim_colors['Ansi 4 Color'].darker(0.2)
    # manim.PURE_RED = ManimColor("#FF0000")
    manim.RED = theme_manim_colors['Ansi 4 Color']


    manim.MAROON_A = theme_manim_colors['Ansi 9 Color'].lighter(0.2)
    manim.MAROON_B = theme_manim_colors['Ansi 9 Color'].lighter(0.1)
    manim.MAROON_C = theme_manim_colors['Ansi 9 Color']
    manim.MAROON_D = theme_manim_colors['Ansi 9 Color'].darker(0.1)
    manim.MAROON_E = theme_manim_colors['Ansi 9 Color'].darker(0.2)
    manim.MAROON = theme_manim_colors['Ansi 9 Color']

    manim.PURPLE_A = theme_manim_colors['Ansi 5 Color'].lighter(0.2)
    manim.PURPLE_B = theme_manim_colors['Ansi 5 Color'].lighter(0.1)
    manim.PURPLE_C = theme_manim_colors['Ansi 5 Color']
    manim.PURPLE_D = theme_manim_colors['Ansi 5 Color'].darker(0.1)
    manim.PURPLE_E = theme_manim_colors['Ansi 5 Color'].darker(0.2)
    manim.PURPLE = theme_manim_colors['Ansi 5 Color']


    manim.PINK =  theme_manim_colors['Ansi 5 Color']
    manim.LIGHT_PINK =  theme_manim_colors['Ansi 13 Color']

    manim.ORANGE = 0.5 * manim.RED + 0.5 * manim.YELLOW
    manim.LIGHT_BROWN = manim.ORANGE.lighter(0.1)
    manim.DARK_BROWN = manim.ORANGE.darker(0.1)

    manim.GRAY_BROWN = 0.5 * manim.LIGHT_BROWN + 0.5 * manim.GRAY
    manim.GREY_BROWN = 0.5 * manim.LIGHT_BROWN + 0.5 * manim.GREY

    # Colors used for Manim Community's logo and banner

    # LOGO_WHITE = ManimColor("#ECE7E2")
    # LOGO_GREEN = ManimColor("#87C2A5")
    # LOGO_BLUE = ManimColor("#525893")
    # LOGO_RED = ManimColor("#E07A5F")
    # LOGO_BLACK = ManimColor("#343434")

    # set background color
    manim_scene.camera.background_color = theme_manim_colors['Background Color']

    if light_theme:
        # somehow prefixes matter here
        manim.Text.set_default(color=manim.BLACK)
        #m.Text.set_default(color=m.BLACK)
        Text.set_default(color=BLACK)


