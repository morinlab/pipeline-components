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
parser = argparse.ArgumentParser(prog='picard_markdup', 
                                 description = "This tool takes in a coordinate sorted BAM file and generates a markdup'd BAM file from it.")
## create the list of input options here. Add as many as desired.
parser.add_argument("--input_file", required=True, help="Coordinate sorted BAM file")
parser.add_argument("--output_file",required=True,help="Name of output BAM file")
parser.add_argument("--metrics_file",required=True,help="Name of output Metrics file")                    

## parse the argument parser.
args, unknown = parser.parse_known_args()
