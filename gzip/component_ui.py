"""
component_ui.py

@author: ppararaj
"""

import argparse

parser = argparse.ArgumentParser(prog='gzip',
                                 description="""Compresses file.""")

parser.add_argument("input_file", help="File to be compressed.")

args, unknown = parser.parse_known_args()
