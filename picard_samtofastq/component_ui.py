"""
component_ui.py

@author: jgrewal
Note the places you need to change to make it work for you. 
They are marked with keyword 'TODO'.
"""

java -Xmx4G -jar /s

import argparse

#==============================================================================
# make a UI 
#==============================================================================
## TODO: pass the name of the component to the 'prog' parameter and a
## brief description of your component to the 'description' parameter.
parser = argparse.ArgumentParser(prog='picard_samtofastq', 
                                 description = "This tool takes in a bam file and generates fastq file(s) from it")

## TODO: create the list of input options here. Add as many as desired.
parser.add_argument(
                    "-x", "--xparam", 
                    default = None, 
                    help= """
                    help message goes here.
                    """)
                    

## parse the argument parser.
args, unknown = parser.parse_known_args()
