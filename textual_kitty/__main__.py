#!/usr/bin/env python

"""Run the textual_kitty demo."""

import sys
from argparse import ArgumentParser
from importlib.util import find_spec

from textual_kitty.demo.renderable import RenderingMethods

textual_available = bool(find_spec("textual"))
default_mode = "rich" if find_spec("textual") is None else "textual"

parser = ArgumentParser(description="Demo the capabilities of textual-kitty")
parser.add_argument("mode", choices=["rich", "textual"], nargs="?", default=default_mode)
parser.add_argument("-m", "--method", choices=[m.name for m in RenderingMethods], default="auto")
arguments = parser.parse_args()

if arguments.mode == "rich":
    from textual_kitty.demo.renderable import run as run_rich_demo

    run_rich_demo(RenderingMethods[arguments.method])
elif not textual_available:
    sys.stderr.write(
        "Optional Textual dependency not available. Install this package as `textual-kitty[textual]` for Textual support."
    )
else:
    from textual_kitty.demo.widget import RenderingMethods as WidgetRenderingMethods
    from textual_kitty.demo.widget import run as run_textual_demo

    run_textual_demo(WidgetRenderingMethods[arguments.method])
