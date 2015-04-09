"""
component_ui.py
@author: jgrewal
"""

import argparse

#==============================================================================
# make a UI 
#==============================================================================
## pass the name of the component to the 'prog' parameter and a
## brief description of your component to the 'description' parameter.
parser = argparse.ArgumentParser(prog='picard_mergesam', 
                                 description = "This tool merges multiple SAM/BAM files into one file.")

## create the list of input options here. Add as many as desired.
parser.add_argument("--input_dir",required=True,help="Directory where all BAM files to be merged are located.")
parser.add_argument("--output_file",required=True,help="Name of output BAM file")
parser.add_argument("--input_regex",required=False,default='*.bam',help="Pattern to match for batch of input files")
parser.add_argument("--sort_order",required=False,default="coordinate",help="Sort order of output file. Choose from {unsorted, queryname, coordinate}")
parser.add_argument("--use_threading",required=False,default="true",help="Use threading to speed up merging. Choose from {true, false}")
parser.add_argument("--delete_input",required=False,default="false")
## parse the argument parser.
args, unknown = parser.parse_known_args()
