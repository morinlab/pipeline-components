"""
component_ui.py

@author: ppararaj
"""

import argparse

parser = argparse.ArgumentParser(prog='hash_read_names',
                                 description="""Uses hash funciton to check for read name integrity.""")
parser.add_argument('--original_bam',
                    help='Path to original BAM.')
parser.add_argument('--hash_sum_outfile', type=argparse.FileType('w'),
                    help='Output file for the hash sum of original BAM reads.')
parser.add_argument('--hash_sum_infile', type=argparse.FileType('r'),
                    help='File containing a hash sum that will be used to check \
                    integrity of either new fastq or new bam files.')
parser.add_argument('--new_fastqs', nargs='*',
                    help='Path(s) or a single glob to FASTQ files to check for \
                    read name integrity.')
parser.add_argument('--new_bams', nargs='*',
                    help='Path(s) or a single glob to FASTQ files to check for \
                    read name integrity.')
args, unknown = parser.parse_known_args()
