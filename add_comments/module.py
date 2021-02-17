#!/usr/bin/python

import os
import json
import random
import argparse
from pathlib import Path


def gen_comment(path):
    if os.path.isfile(path):
        with open(path) as file:
            return "{}{}{}".format("\n"*random.randint(0, 3), file.read(), "\n"*random.randint(0, 3))
    else:
        raise Exception("Invalid template path")


def add_comments(comment, dir_path, multi=False):
    config_path = os.path.join(Path(__file__).parent, 'config.json')

    with open(config_path) as f:
        config = json.load(f)

    comment_type = "multi" if multi else "single"

    for root, dirs, files in os.walk(dir_path):
        if len(dirs) > 0 and dirs[-1] in config["skip"]["folders"]:
            continue
        for file in files:
            if file in config["skip"]["files"]:
                continue
            file_type = file.split(".")[-1]
            if file_type in config["language"]:
                file_path = os.path.join(root, file)
                with open(file_path, "a") as open_file:
                    open_file.write(
                        '\n' + config["language"][file_type][comment_type]["start"] + '\n')
                    open_file.write(comment)
                    open_file.write(
                        '\n' + config["language"][file_type][comment_type]["end"] + '\n')


def handler():
    parser = argparse.ArgumentParser(prog='addcomments',
                                     description='Add signature to source code')

    parser.add_argument('-multi', action='store_const', const=True,
                        default=False, dest='multiline',
                        help="Multiline comment")
    parser.add_argument('path', help="path to folder")
    parser.add_argument(
        '-template', help="path to template file", default=False)

    args = parser.parse_args()
    if os.path.isdir(args.path):
        comment = None
        comment_type = args.multiline or args.template
        if comment_type:
            comment = gen_comment(args.template)
        else:
            comment = input("Enter content of comment: ")
            while(len(comment) < 1):
                comment = input(
                    "Kindly enter proper input.\nEnter content of comment: ")
        add_comments(comment, args.path, comment_type)
    else:
        print("Enter valid folder directory")
