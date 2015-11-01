"""
component_ui.py

@author: ppararaj
"""

import argparse

parser = argparse.ArgumentParser(prog='merge_mpileup',
                                 description="""Merge mpileup files.""")

parser.add_argument("input_dir", help="Directory containing mpileup files to be merged.")

args, unknown = parser.parse_known_args()
