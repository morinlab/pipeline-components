"""
component_ui.py

Note the places you need to change to make it work for you. 
They are marked with keyword 'TODO'.
"""

import argparse

#==============================================================================
# make a UI 
#==============================================================================
## TODO: pass the name of the component to the 'prog' parameter and a
## brief description of your component to the 'description' parameter.
parser = argparse.ArgumentParser(prog='file_eater', 
                                 description = """This component deletes all the files passed to it. """)

## TODO: create the list of input options here. Add as many as desired.
parser.add_argument("--input_files", required=True,help="List of files to delete") 
parser.add_argument("--out_files", required=True, help="List of output files to compare to first")
parser.add_argument("--filetype_in", required=True, help= "One of bam or fastq")
parser.add_argument("--filetype_out", required=True, help= "One of bam or fastq")
## parse the argument parser.
args, unknown = parser.parse_known_args()
