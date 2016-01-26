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
parser = argparse.ArgumentParser(prog='augmentmaf', 
                                 description = "This tool takes in a maf file and paired bams, and generates an augmented maf output with readcounts.")

## create the list of input options here. Add as many as desired.
parser.add_argument("--input_nbam", required=True, help="Input normal bam.")
parser.add_argument("--input_tbam", required=True, help="Input tumour bam.")
parser.add_argument("--input_maf", required=True, help="Input maf file.")
parser.add_argument("--reference", required=True, help="Input reference.")
parser.add_argument("--output_augmaf", required=True, help="Output augmaf'd file name.")

## parse the argument parser.
args, unknown = parser.parse_known_args()
