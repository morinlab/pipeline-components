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
parser = argparse.ArgumentParser(prog='clipoverlap', 
                                 description = "This tool generates a softclipped BAM from an input BAM file.")

## create the list of input options here. Add as many as desired.
parser.add_argument("--input_file",required=True,help="Input BAM file")
parser.add_argument("--output_file",required=True,help="Name of output BAM file")
                    

## parse the argument parser.
args, unknown = parser.parse_known_args()
