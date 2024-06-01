#!/usr/bin/env python3
"""Generate colors of this theme."""

import math
import pathlib
import re

import cv2
import jinja2
import numpy

THIS_DIR = pathlib.Path(__file__).absolute().parent

# Map from level to lightness.
LIGHTNESS_MAP = {
    1: 99.5,
    50: 97.2,
    100: 93.95,
    200: 85.1,
    300: 76.5,
    400: 67.65,
    500: 57.8,
    600: 47.6,
    700: 37.4,
    800: 27.2,
    900: 17.0,
    950: 7.0,
}


RGB_CODE_REGEX = re.compile(r"#([0-9A-F][0-9A-F])([0-9A-F][0-9A-F])([0-9A-F][0-9A-F])")


def rgb_code_to_lch(code: str) -> tuple[float, float, float]:
    """Convert an RGB color code to a color in LCh color space.

    Args:
        code (str): Color code.

    Returns:
        tuple[float, float, float]: Color in LCh color space.
    """
    match = RGB_CODE_REGEX.match(code)
    if not match:
        raise ValueError(f"Invalid RGB code: {code}")

    r = int(match.group(1), 16)
    g = int(match.group(2), 16)
    b = int(match.group(3), 16)

    rgb_mat = numpy.array([[[r / 255.0, g / 255.0, b / 255.0]]], dtype=numpy.float32)
    lab_mat = cv2.cvtColor(rgb_mat, cv2.COLOR_RGB2Lab)
    l = lab_mat[0][0][0]
    a = lab_mat[0][0][1]
    b = lab_mat[0][0][2]
    c = math.sqrt(a * a + b * b)
    h = math.atan2(b, a) * 180 / math.pi
    if h < 0.0:
        h += 360.0
    return l, c, h


def lch_to_rgb_code(l: float, c: float, h: float) -> str:
    """Convert a color in LCh color space to an RGB color code.

    Args:
        l (float): Lightness.
        c (float): Chroma.
        h (float): Hue.

    Returns:
        str: Color code.
    """
    a = c * math.cos(h * math.pi / 180.0)
    b = c * math.sin(h * math.pi / 180.0)
    lab_mat = numpy.array([[[l, a, b]]], dtype=numpy.float32)
    rgb_mat = cv2.cvtColor(lab_mat, cv2.COLOR_Lab2RGB)
    r = int(rgb_mat[0][0][0] * 255.0)
    g = int(rgb_mat[0][0][1] * 255.0)
    b = int(rgb_mat[0][0][2] * 255.0)
    return f"#{r:02x}{g:02x}{b:02x}"


def to_gray(origin: str) -> tuple[float, float, float]:
    """Convert to gray color.

    Args:
        origin (str): Original color.

    Returns:
        tuple[float, float, float]: Gray color.
    """
    l, _, h = rgb_code_to_lch(origin)
    return l, 10.0, h


# Map from name of the original color to the original color.
# (The original color is the color to use in calculation of colors.)
ORIGINAL_COLOR_MAP = {
    "primary": rgb_code_to_lch("#D4682A"),
    "secondary": rgb_code_to_lch("#F0C403"),
    "accent": rgb_code_to_lch("#3BB111"),
    "gray": to_gray("#DE6316"),
    "info": rgb_code_to_lch("#3BB111"),
    "warning": rgb_code_to_lch("#F0C403"),
    "danger": rgb_code_to_lch("#CB0541"),
}


def calculate_color(original_color_name: str, level: int) -> str:
    """Calculate a color.

    Args:
        original_color_name (str): Name of the original color.
        level (int): Level.

    Returns:
        str: Calculated color.
    """
    l_origin, c_origin, h = ORIGINAL_COLOR_MAP[original_color_name]
    l = LIGHTNESS_MAP[level]
    if l < l_origin:
        c = c_origin * (l / l_origin)
    else:
        c = c_origin * ((100.0 - l) / (100.0 - l_origin))
    return lch_to_rgb_code(l, c, h)


def generate_colors_css() -> None:
    """Generate CSS file of colors."""
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(str(THIS_DIR)))
    template = env.get_template("sphinx-orange-book-theme-colors.css.jinja")
    css = template.render(calculate_color=calculate_color)
    with open(
        str(
            THIS_DIR.parent
            / "sphinx_orange_book_theme"
            / "static"
            / "styles"
            / "sphinx-orange-book-theme-colors.css"
        ),
        mode="w",
        encoding="utf-8",
    ) as file:
        file.write(css)


if __name__ == "__main__":
    generate_colors_css()
