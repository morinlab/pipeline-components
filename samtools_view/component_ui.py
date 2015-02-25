"""
component_ui.py
@author:jgrewal
"""

import argparse

#==============================================================================
# make a UI 
#==============================================================================
## pass the name of the component to the 'prog' parameter and a
## brief description of your component to the 'description' parameter.
parser = argparse.ArgumentParser(prog='samtools_view', 
                                 description = "This tool takes in a bam file and passes it to samtools view with options. Instead of options, you can also pass 'splitbam=True' if you wish to split your bam into paired and unpaired reads")

## create the list of input options here. Add as many as desired.
parser.add_argument("--input_file", required=True, help="Bam file to be passed to samtools view") 
parser.add_argument("--output_file", required=True, help="Name of output bam file")
parser.add_argument("--options", required=False,default="", help="List of all options to append to samtools view, except input and output files")
parser.add_argument("--splitbam",required=False,default=False,help="Set this to true if you wish to split your bam into paired and unpaired reads") 

## parse the argument parser.
args, unknown = parser.parse_known_args()
