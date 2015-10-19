"""
component_ui.py

@author: bgrande
"""

import argparse

parser = argparse.ArgumentParser(prog='bwa_mem',
                                 description="""Run BWA-MEM alignment on FASTQ files.""")

parser.add_argument("reference", help="Ensembl VEP-annotated VCF file")
parser.add_argument("fastq_1", help="First FASTQ file")
parser.add_argument("--fastq_2", help="Second FASTQ file")
parser.add_argument("--num_threads", help="Number of threads")

args, unknown = parser.parse_known_args()
