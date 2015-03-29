"""
component_ui.py

@author: autogen_component.py
"""

import argparse
parser = argparse.ArgumentParser(
    description="Convert a BAM file into FASTQ file(s)")
parser.add_argument("input_bam", help="Input BAM file")
parser.add_argument("output_fastq", help="Output FASTQ file")

args, unknown = parser.parse_known_args()
