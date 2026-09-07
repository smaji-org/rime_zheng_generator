#!/usr/bin/env python3

# generator.py
# -----------
# Copyright : (c) 2023 - 2026, smaji.org
# Copyright : (c) 2023 - 2026, ZAN DoYe <zandoye@gmail.com>
# Licence   : GPL2
#
# This file is a part of rime_zheng_generator.


import os
import sys
import argparse

import blocks
import rime_config
from pathlib import Path
from datetime import datetime, timezone

from typing import TextIO

description= ('''Smaji 鄭碼
碼表源自鄭碼發明人以及熱心用戶的貢獻''')
 
opt_parser= argparse.ArgumentParser()

opt_parser.add_argument("--cjkv_info", type= str,
    help= "the path of cjkv_info")
opt_parser.add_argument("--name", type= str,
    help= "the name of the code table")
opt_parser.add_argument("--verbose", type= str,
    help= "generate verbose info")
opt_parser.add_argument("--region", type= str,
    help= "the region from where to select characters")
opt_parser.add_argument("--description", type= str,
    help= "the description of this zhengma input method")
opt_parser.add_argument("--version", type= str, required= True,
    help= "the version of the code table")
opt_parser.add_argument("--comment", type= str,
    help= "the comment of this version")
opt_parser.add_argument("--datetime", type= str,
    help= "the datetime of this version")
opt_parser.add_argument("--input", type= str,
    help= "the directory of the input method collection")
opt_parser.add_argument("--output", type= str,
    help= "the directory containing the new code table")

class Opts:
    def __init__(self):
        now_str= datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        self.cjkv_info: str= "."
        self.name: str= "smaji_zheng"
        self.region: list[str]= [
            "China",
            "Hong Kong",
            "Japan",
            "Macau",
            "North Korea",
            "South Korea",
            "Taiwan",
            "Vietnam",
            "United Kingdom",
            "N/A"
            ]
        self.description: str= description
        self.version: str= ""
        self.comment: str= ""
        self.datetime: str= now_str
        self.input: str= "."
        self.output: str= "."
        self.verbose= False

def mystr(v)-> str:
    return str(v) if v else ""

def setup_opt() -> Opts:
    opts= Opts()
    args= opt_parser.parse_args()
    opts.cjkv_info= mystr(args.cjkv_info) or opts.cjkv_info
    opts.name= mystr(args.name) or opts.name
    opts.region= mystr(args.region).split(",") or opts.region
    opts.description= mystr(args.description) or opts.description
    opts.version= mystr(args.version)
    opts.comment= mystr(args.comment) or opts.comment
    opts.datetime= mystr(args.datetime) or opts.datetime
    opts.input= mystr(args.input) or opts.input
    opts.output= mystr(args.output) or opts.output
    if args.verbose is None:
        opts.verbose= False
    else:
        opts.verbose= not str(args.verbose).lower() in ["n", "no", "none", "f", "false"]
    try:
        os.makedirs(os.path.join(opts.output, "data"), exist_ok= True)
    except OSError:
        pass
    return opts

def record_a_char(file: TextIO, char_dir: Path, core: int, verbose=False):
    if char_dir.exists():
        core= int(char_dir.name, base=16)
        for glyph_dir in char_dir.iterdir():
            char= chr(core)
            variation= int(glyph_dir.name, base=16)
            if variation != 0:
                char= char + chr(variation)
            with open(glyph_dir/"zhengma", "r") as file_zhengma:
                zhengma_list= file_zhengma.readlines()
                for zhengma in zhengma_list:
                    zhengma= zhengma.strip()
                    if verbose:
                        item="{}\t{} # {:x}:{:x}\n".format(
                            char, zhengma,
                            core, variation)
                    else:
                        item="{}\t{}\n".format(char, zhengma)
                    file.write(item)


def record_a_block(file: TextIO, dir: Path, block_name: str, verbose=False):
    block= blocks.blocks_current.get(block_name)
    if block:
        for char in range(*block):
            char_dir= dir / "{:x}".format(char)
            record_a_char(file, char_dir, char, verbose)

def record_dict(file: TextIO, dir: str, verbose=False):
    dict_dir= Path(dir) / "glyph"
    for block in blocks.blocks_current.keys():
        record_a_block(file, dict_dir, block, verbose)

if __name__ == "__main__":
    opts= setup_opt()
    main_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

    with open(os.path.join(opts.output, "description"), "w") as output_file:
        output_file.write(opts.description)
    with open(os.path.join(opts.output, "version"), "w") as output_file:
        output_file.write(opts.version)
    with open(os.path.join(opts.output, "comment"), "w") as output_file:
        output_file.write(opts.comment)
    with open(os.path.join(opts.output, "datetime"), "w") as output_file:
        output_file.write(opts.datetime)

    with open(os.path.join(opts.output, "data", opts.name + ".dict.yaml"), "w") as output_file:
        output_file.write(rime_config.header.format(opts.name, opts.version))
        record_dict(output_file, opts.input, opts.verbose)
        with open(os.path.join(main_dir, "word"), "r") as word_file:
            with open(os.path.join(main_dir, "comp"), "r") as comp_file:
                output_file.write("\n")
                output_file.write(word_file.read())
                output_file.write("\n")
                output_file.write(comp_file.read())

    with open(os.path.join(opts.output, "data", opts.name + ".schema.yaml"), "w") as output_file:
        output_file.write(rime_config.schema.format(opts.name, opts.version, opts.name))

