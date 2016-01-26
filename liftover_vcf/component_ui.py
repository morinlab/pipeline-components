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
parser = argparse.ArgumentParser(prog='liftover_vcf', 
                                 description = "This wrapper for the gatk liftoverVCF.pl script converts vcfs derived from an old reference aligned BAM to a new reference.")

## create the list of input options here. Add as many as desired.
parser.add_argument("--input_vcf",required=True,help="Input vcf file.")
parser.add_argument("--output_file",required=True,help="Output vcf file.")
parser.add_argument("--chain_file",required=True,help="Chain file for gatk tool.")
parser.add_argument("--old_ref",required=True,help="Old reference file to which the variants is aligned.")                    
parser.add_argument("--new_ref",required=True,help="New reference file to which you want the variants to be aligned.")
## parse the argument parser.
args, unknown = parser.parse_known_args()
