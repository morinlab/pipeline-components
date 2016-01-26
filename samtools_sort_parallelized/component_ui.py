"""
component_ui.py

@author: ppararaj
"""

import argparse

parser = argparse.ArgumentParser(prog='samtools_sort_parallelized',
                                 description="""Sort BAM file.""")

parser.add_argument("input_dir", help="Unsorted BAM file directory.")
parser.add_argument("output_dir", help="Output directory.")

args, unknown = parser.parse_known_args()
