"""
component_ui.py

@author: autogen_component.py
"""

import argparse
parser = argparse.ArgumentParser(
    description="Convert between different file types.")
parser.add_argument(
    "input_type", nargs=1, help="cancer_api file type for input file(s)")
parser.add_argument(
    "input_parser", nargs=1, help="cancer_api parser for input file")
parser.add_argument(
    "output_type", nargs=1, help="cancer_api file type for output file")
parser.add_argument(
    "input_files", nargs="+", help="List of input file(s) (same type)")
parser.add_argument(
    "--output_dir", help="Output all converted files in this directory")

args, unknown = parser.parse_known_args()
