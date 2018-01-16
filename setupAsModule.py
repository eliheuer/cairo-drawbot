#!/usr/bin/env python
from __future__ import division, absolute_import, print_function
from setuptools import setup
import os
import shutil

from drawBot.drawBotSettings import __version__

try:
    import fontTools
except ImportError:
    print("*** Warning: drawBot requires FontTools, see:")
    print("    https://github.com/fonttools/fonttools")

