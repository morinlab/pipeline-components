"""
component_ui.py

@author: ppararaj
"""

import argparse

parser = argparse.ArgumentParser(prog='samtools_mpileup',
                                 description="""Run samtools mpileup.""")

parser.add_argument("input_bam", help="BAM file to pileup")
parser.add_argument("f", help="Reference FASTA file.")
args, unknown = parser.parse_known_args()
