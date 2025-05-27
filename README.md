[![PyPI version](https://img.shields.io/pypi/v/manim-themes)](https://pypi.org/project/manim-themes/)
![License](https://img.shields.io/pypi/l/manim-themes)
[![Documentation Status](https://readthedocs.org/projects/manim-themes/badge/?version=latest)](https://manim-themes.readthedocs.io/en/latest/?badge=latest)

<h1 align="center">
  <img src="https://raw.githubusercontent.com/Alexander-Nasuta/manim-themes/master/resources/ThemeGif_ManimCE_v0.19.0.gif" alt="Example Themes" />
</h1>

## About this Project

This project is a Python Module that provides allows theming of [Manim](https://www.manim.community) projects with [iterm2 color themes](https://iterm2colorschemes.com).
It works by overriding the default Manim configuration with a set of colors that are derived from the selected theme.
I am not an expert in how Python looks up variables, and I am not sure if there is a better way for a plugin to realise theming.
It works fine for my purposes, but if you have a idea how to improve this, feel free to let me know (by issuing a pull request or opening an issue).
## Installation

Install the package with pip:
```
   pip install manim-themes
```


## Minimal Example

**NOTE: Please make sure you have manim installed and running on your machine**

Below is a minimal example of how to use the Module.

```python
import manim as m

from manim_themes.manim_theme import apply_theme


class MinimalThemeExample(m.Scene):

    def setup(self):
        # Set the background color to a light beige
        theme = "Andromeda"
        apply_theme(manim_scene=self, theme_name=theme, light_theme=True)

    def construct(self):
        my_text = m.Text("Hello World")
        maroon_text = m.Text("I use Manim BTW", color=m.MAROON)
        maroon_text.next_to(my_text, m.DOWN)

        text_group = m.VGroup(my_text, maroon_text).move_to(m.ORIGIN)

        self.play(m.FadeIn(text_group))


if __name__ == '__main__':
    import os
    from pathlib import Path

    FLAGS = "-pqm"
    SCENE = "MinimalThemeExample"

    file_path = Path(__file__).resolve()
    os.system(f"manim {Path(__file__).resolve()} {SCENE} {FLAGS}")
```

This should yield a Scene that looks like so:

![Example Output Screenshot](https://raw.githubusercontent.com/Alexander-Nasuta/manim-themes/master/resources/MinimalThemeExample_ManimCE_v0.19.0.png)


### Documentation

This project uses `sphinx` for generating the documentation.
It also uses a lot of sphinx extensions to make the documentation more readable and interactive.
For example the extension `myst-parser` is used to enable markdown support in the documentation (instead of the usual .rst-files).
It also uses the `sphinx-autobuild` extension to automatically rebuild the documentation when changes are made.
By running the following command, the documentation will be automatically built and served, when changes are made (make sure to run this command in the root directory of the project):

```shell
sphinx-autobuild ./docs/source/ ./docs/build/html/
```

If sphinx extensions were added the `requirements_dev.txt` file needs to be updated.
These are the requirements, that readthedocs uses to build the documentation.
The file can be updated using this command:

```shell
poetry export -f requirements.txt --output requirements.txt --with dev
```

This project features most of the extensions featured in this Tutorial: [Document Your Scientific Project With Markdown, Sphinx, and Read the Docs | PyData Global 2021](https://www.youtube.com/watch?v=qRSb299awB0).
