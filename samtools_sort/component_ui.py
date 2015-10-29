"""
component_ui.py

@author: ppararaj
"""

import argparse

parser = argparse.ArgumentParser(prog='samtools_sort',
                                 description="""Sort BAM file.""")

parser.add_argument("input_bam", help="Unsorted BAM file.")
parser.add_argument("output_bam", help="Sorted BAM file.")

args, unknown = parser.parse_known_args()
