"""
component_ui.py

@author: ppararaj
"""

import argparse


parser = argparse.ArgumentParser(prog='pysam_bam2fq',
                                 description="""Converts BAM to FASTQ.""")
parser.add_argument('bam', help='BAM to convert to FASTQ.')
parser.add_argument('output_dir', default='./',
                    help='Output directory of the FASTQ files.')
parser.add_argument('interval_file', type=argparse.FileType('w'),
                    help='Interval file that will be created.')
parser.add_argument('--num_reads', '-n', type=int, default=75000000,
                    help='Maximum number of reads per FASTQ file.')
args, unknown = parser.parse_known_args()
