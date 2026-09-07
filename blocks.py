#!/usr/bin/env python3

# blocks.py
# -----------
# Copyright : (c) 2023 - 2026, smaji.org
# Copyright : (c) 2023 - 2026, ZAN DoYe <zandoye@gmail.com>
# Licence   : GPL2
#
# This file is a part of rime_zheng_generator.

blocks_test: dict[str, tuple[int, int]]= {
    "basic" : (0x04E00, 1+ 0x4EFF),
    "a"     : (0x03400, 1+ 0x34FF),
    }

blocks_13: dict[str, tuple[int, int]]= {
    "basic" : (0x04E00, 1+ 0x9FFC),
    "a"     : (0x03400, 1+ 0x4DBF),
    "b"     : (0x20000, 1+ 0x2A6DF),
    "c"     : (0x2A700, 1+ 0x2B738),
    "d"     : (0x2B740, 1+ 0x2B81D),
    "e"     : (0x2B820, 1+ 0x2CEA1),
    "f"     : (0x2CEB0, 1+ 0x2EBE0),
    "g"     : (0x30000, 1+ 0x3134A),
    }

blocks_versions= {
    13: blocks_13,
    }

blocks_current= blocks_13

