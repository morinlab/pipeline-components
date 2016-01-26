"""
component_ui.py

@author: autogen_component.py
"""

import argparse
parser = argparse.ArgumentParser(description="Split FASTQ files into smaller ones.")
parser.add_argument("fastq", nargs="+", help="FASTQ file(s) (single- or paired-end)")
parser.add_argument("--num_reads", "-n", type=int, default=75000000,
help="Number of reads per output FASTQ file")
parser.add_argument("--num_buffer", "-b", type=int, default=5000000,
help="Number of reads kept in buffer before flushing to disk")
parser.add_argument("--output_dir", default=".", help="Output directory")
parser.add_argument("--interval_file", help="Output intervals (for use in Pipeline Factory)")
parser.add_argument("--no_compression", action="store_true",
help="Disables gzip compression of output FASTQ files")

args, unknown = parser.parse_known_args()

