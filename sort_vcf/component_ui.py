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
parser = argparse.ArgumentParser(prog='sort_vcf', 
                                 description = "This component takes a vcf file and sorts variants karyotypically. Generally this is a required pre-processing step for liftoverVCF.")

## create the list of input options here. Add as many as desired.
parser.add_argument("--input_file",required=True,help="Input vcf file.")
parser.add_argument("--output_file",required=True,help="Output file.")
parser.add_argument("--ref_fai",required=True,help=".fai file with contigs in desired sorting order")
#                 'input_param3' : None
## parse the argument parser.
args, unknown = parser.parse_known_args()
