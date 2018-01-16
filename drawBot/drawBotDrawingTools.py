from __future__ import absolute_import

import math
import os
import random


def _getmodulecontents(module, names=None):
    d = {}
    if names is None:
        names = [name for name in dir(module) if not name.startswith("_")]
    for name in names:
        d[name] = getattr(module, name)
    return d


_chachedPixelColorBitmaps = {}


_paperSizes = {
    'Letter'      : (612, 792),
    'LetterSmall' : (612, 792),
    'Tabloid'     : (792, 1224),
    'Ledger'      : (1224, 792),
    'Legal'       : (612, 1008),
    'Statement'   : (396, 612),
    'Executive'   : (540, 720),
    'A0'          : (2384, 3371),
    'A1'          : (1685, 2384),
    'A2'          : (1190, 1684),
    'A3'          : (842, 1190),
    'A4'          : (595, 842),
    'A4Small'     : (595, 842),
    'A5'          : (420, 595),
    'B4'          : (729, 1032),
    'B5'          : (516, 729),
    'Folio'       : (612, 936),
    'Quarto'      : (610, 780),
    '10x14'       : (720, 1008),
}

for key, (w, h) in list(_paperSizes.items()):
    _paperSizes["%sLandscape" % key] = (h, w)
