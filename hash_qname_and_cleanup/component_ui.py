"""
component_ui.py

@author: ppararaj
"""

import argparse

parser = argparse.ArgumentParser(prog='hash_qname_and_cleanup',
                                 description="""Uses hash to check for read name integrity and removes intermediate files.""")
parser.add_argument('--original_bam', nargs='?',
                    help='BAM that will be realigned.')
parser.add_argument('--read_set_out', nargs='?',
                    help='Filename of serialized read name set of original bam file.')
parser.add_argument('--read_set', nargs='?',
                    help='File containing reads of the original BAM.')
parser.add_argument('--files_to_delete_path', nargs='?', default='./',
                    help='Path to directory of files to delete indicated by --files_to_delete \
                    parameter. [./]')
parser.add_argument('--files_to_delete', nargs='*',
                    help='Filename(s) or glob of files to delete.')
parser.add_argument('--new_file_path', nargs='?', default = './',
                    help='Path to directory of location of new files (BAMs or FASTQs). [./]')
parser.add_argument('--new_bam_filename', nargs='*',
                    help='BAM filename(s) or glob that will undergo read counting to \
                    check for read integrity.')
parser.add_argument('--new_fastq_filename', nargs='*',
                    help='FASTQ filename(s) or glob that will undergo read counting to \
                    check for read integrity.')
args, unknown = parser.parse_known_args()
