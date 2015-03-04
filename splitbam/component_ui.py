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
parser = argparse.ArgumentParser(prog='splitbam', 
                                 description = "This tool takes in a bam file and splits it into two bams, ones with paired and unpaired reads")

## create the list of input options here. Add as many as desired.
parser.add_argument("--input_file",required=True,help="Bam file to be split")
parser.add_argument("--output_dir",required=False,default="./", help="Output directory for results. Default is current directory")
parser.add_argument("--samflag",required=False,default="8",help="Samflag to split bams on. Default is 8 (unmapped mate)") 

## parse the argument parser.
args, unknown = parser.parse_known_args()
