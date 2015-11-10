"""
component_ui.py

@author: ppararaj
"""

import argparse

parser = argparse.ArgumentParser(prog='samtools_merge',
                                 description="""Merge BAM files.""")

parser.add_argument("input_dir", help="Sorted BAM file directory.")
parser.add_argument("output_file", help="Merged output BAM file.")

args, unknown = parser.parse_known_args()
