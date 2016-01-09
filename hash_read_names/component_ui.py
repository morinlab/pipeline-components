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
                    help='Output file for the hash sum.')
parser.add_argument('--hash_sum_infile', type=argparse.FileType('r'),
                    help='File containing a hash sum that will be used to check \
                    integrity of either new fastq or new bam files.')
parser.add_argument('--directory',
                    help='Directory containing FASTQ or BAM files to hash.')
parser.add_argument('--files', nargs='*',
                    help="FASTQ or BAM files in '--directory' to hash. Can be a glob.")
parser.add_argument('--new_fastqs', action=store_true,
                    help="Flag indicating files specified in '--files' are FASTQs.")
parser.add_argument('--new_bams', action=store_true,
                    help="Flag indicating files specified in '--files' are BAMs.")

args, unknown = parser.parse_known_args()
