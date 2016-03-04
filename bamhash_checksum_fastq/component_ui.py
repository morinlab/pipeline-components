"""
component_ui.py

@author: ppararaj
"""

import argparse

parser = argparse.ArgumentParser(prog='bamhash_checksum_fastq',
                                 description="""Hash FASTQ files 
                                 to verify data integrity""")

parser.add_argument('read_fastq1', required=True,  
                    help="""First fastq file""")
parser.add_argument('read_fastq2', required=False,
                    help="""Second (optional) fastq file""")
parser.add_argument('out_checksum', help="""output checksum file""")
parser.add_argument('-d', '--debug', 
                    help="""Debug mode. Prints full hex for each read to stdout""")
parser.add_argument('-R', '--no-readnames',
                    help="""Do not use read names as part of checksum""")
parser.add_argument('-Q', '--no-quality',
                    help="""Do not use read quality as part of checksum""")
parser.add_argument('-P', '--no-paired',
                    help="""Bam files were not generated with paired-end reads""")

# May have to add output file argument
args, unknown = parser.parse_known_args()
