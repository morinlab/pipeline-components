"""
component_ui.py

@author: ppararaj
"""

import argparse


parser = argparse.ArgumentParser(prog='bam2fq',
                                 description="""Converts BAM to FASTQ.""")

# Required Arguments
parser.add_argument('bam', help='Specify BAM file.')
parser.add_argument("outdir", help='output directory')

# Optional Arguments
parser.add_argument('--num_reads', '-n', default=75000000,
					help='Specify number of reads per FASTQ file.')

args, unknown = parser.parse_known_args()
